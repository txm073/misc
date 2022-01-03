import os
import tarfile
import shutil
import gzip
import pkg_resources
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import re

r"""
1. Search for desired package on PyPi
2. Get top result, go to project page: https://pypi.org/project/<project>
3. Find .gz source file download link (not wheels) and copy file name
4. Get href for link, then redirect and download compressed folder
5. Extract folder and move it to Python Lib folder
"""

def find_import_folder(base_folder, import_name):
    found = None
    folders = []
    for root, dirs, files in os.walk(base_folder):
        for name in dirs:
            folders.append(os.path.abspath(os.path.join(root, name)).replace("\\", "/").replace("//", "/"))
            if name == import_name:
                found = os.path.abspath(os.path.join(root, name)).replace("\\", "/").replace("//", "/")

    if found:
        return found
    probs = [fuzz.ratio(os.path.basename(path), import_name) for path in folders]
    return folders[probs.index(max(probs))]

def get_dependencies(package):
    try:
        package = pkg_resources.working_set.by_key[package]
        return [re.split("[\>\=,\~\=,\<,\>,\<=,\=\=]", str(r))[0] for r in package.requires()]
    except KeyError:
        print(f"Warning: Some dependencies for package '{package}' may not be installed. You may have to manually install them from PyPi.")
        return []

def find_import_name(text_box, package_name):
    easy_package = text_box.find("span", class_="nn", recursive=True)
    if easy_package:
        return easy_package.getText().strip()
    chars = text_box.findAll("span")
    if chars:
        code = "".join([c.getText().strip() for c in chars]).split(">>>")
        import_lines = [line for line in code if line.startswith("import") or line.startswith("from")]
        packages = [line.split(".")[0].replace("import", "").replace("from", "") for line in import_lines]

    else:
        text = text_box.find("code")
        code = [line.replace(">>>", "").strip() for line in text.getText().split("\n") if ">>>" in line]
        import_lines = [line for line in code if line.startswith("import") or line.startswith("from")]
        packages = [line.split(" ")[1].split(".")[0] for line in import_lines]

    probs = [fuzz.ratio(package, package_name) for package in packages]
    package = packages[probs.index(max(probs))]
    return package

def install(package, path=os.path.expandvars(r"C:/Users/$USERNAME/Downloads/"), packages_folder=None, move=True, delete_after=True, verbose=True, rlevel=0):    
    if verbose:
        print()
        print("PACKAGE:", package)
        print("PATH:", path)
        print("FOLDER:", packages_folder)
        print("RECURSION LEVEL:", rlevel)
        print(f"Searching for '{package}' on PyPi...")
    if path == ".":
        move = False
    search_url = f"https://pypi.org/search/?q={package}"
    resp = requests.get(search_url) 
    driver = BeautifulSoup(resp.text, "lxml")
    packages = driver.findAll(class_="package-snippet")
    search = re.search(r'href\=\".*\"', str(packages[0]))
    rel_url = str(packages[0])[search.span()[0]:search.span()[1]][6:-1]
    project_url = "https://pypi.org" + rel_url
    if verbose:
        print(f"Located project '{project_url.split('/')[-2]}'")

    if verbose:
        print("Parsing description data...")

    try:
        resp = requests.get(project_url + "#description")
        driver = BeautifulSoup(resp.text, "lxml")
        text_boxes = driver.findAll("pre")
        box_sizes = [length for length in [len(str(box)) for box in text_boxes]]
        text_box = text_boxes[box_sizes.index(max(box_sizes))]    
        import_name = find_import_name(text_box, package)
    except (AttributeError, ValueError):
        import_name = driver.find("span", id="pip-command").getText().split(" ")[-1]

    if verbose:
        print("Located Python import name:", import_name)
    
    resp = requests.get(project_url + "#files")
    driver = BeautifulSoup(resp.text, "lxml")
    table = driver.find(class_="table table--downloads")
    table_body = table.find("tbody")
    rows = table_body.findAll("tr")
    for index, row in enumerate(rows):
        header = row.find("th")
        link = header.find("a")["href"]
        info = [elem for elem in re.sub(" +", "", str(row.getText())).split("\n") if elem != ""]
        fname, fsize, _, ftype = info[1:5]
        if ftype == "Source" and fname.endswith(".tar.gz"):
            if verbose:
                print("Located zip archive")
            break
    
    if verbose:
        print("Downloading zip archive...")
    resp = requests.get(link)
    path += fname
    if verbose:
        print("Download completed successfully. Unzipping folder...")

    unzipped = fname.replace(".zip", "").replace(".gz", "").replace(".tar", "")
    #os.chdir(os.path.dirname(dst))
    with open(path, "wb") as f:
        f.write(resp.content)
    download = os.path.join(os.getcwd(), unzipped).replace("\\", "/")

    if fname.endswith("tar.gz"):
        tar = tarfile.open(path, "r:gz")
        tar.extractall()
        tar.close()
    elif fname.endswith("tar"):
        tar = tarfile.open(path, "r:")
        tar.extractall()
        tar.close()
    elif fname.endswith(".zip"):
        with open(path, "rb") as f_in:
            with gzip.open(download, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
    if verbose:
        print(f"Successfully extracted folder to '{download}'")

    import_folder = find_import_folder(download, import_name)
    if verbose:
        print("Located import folder:", import_folder)
        print(f"Moving import folder '{import_folder}' to '{packages_folder}'")
            
    try:    
        shutil.move(import_folder, packages_folder)
    except shutil.Error as e:
        if "already exists" not in str(e):
            raise

    if re.search("\d_\d", str(os.path.basename(import_folder))):
        os.rename(packages_folder + "/" + os.path.basename(import_folder), packages_folder + "/" + package)

    deps = get_dependencies(import_name)
    if deps:
        if verbose:
            print("Installing dependencies:", ", ".join(deps))
        for dep in deps:
            if dep == package:
                continue
            install(dep, path=path.replace(fname, ""), packages_folder=packages_folder, move=move, verbose=verbose, delete_after=delete_after, rlevel=rlevel+1)

    if delete_after:
        try:
            shutil.rmtree(download)
        except Exception as e:
            print(f"An exception occured when removing excess installation files for package '{package}'")

    if not move:
        return True
    if package in os.listdir(download):
        shutil.move(os.path.join(download, package).replace("\\", "/"), os.path.join(os.getcwd(), package).replace("\\", "/"))
        shutil.rmtree(download)
    else:
        for folder in [item for item in os.listdir(download) 
                        if os.path.isdir(os.path.join(download, item).replace("\\", "/"))]:
            shutil.move(os.path.join(download, folder).replace("\\", "/"), os.path.join(os.getcwd(), folder).replace("\\", "/"))
        shutil.rmtree(download)

    os.remove(path)

    if verbose:
        print(f"Extracted '{fname}' to '{os.getcwd()}'")

#install("requests", move=False, packages_folder="C:/Users/User/Desktop/pypi-packages", verbose=True)

import pkg_resources
  
def get_dependencies(package_name, tree=True, rlevel=1, pre=False):
    try:
        package = pkg_resources.working_set.by_key[package_name]
    except KeyError:
        return None
    deps = [re.split("[^A-Za-z0-9\- ]", str(r))[0] for r in package.requires()]
    if pre:
        return deps
    if rlevel == 1:
        if tree:
            print(package_name + ":" if deps else package_name)
        global global_deps 
        global_deps = []
    for dep in deps:
        output = ("  " * rlevel) + "- " + dep
        if tree:
            print(output + ":" if get_dependencies(dep, tree=tree, pre=True) else output)
        global_deps.extend(get_dependencies(dep, tree=tree, rlevel=rlevel+1))
        
    if rlevel != 1:
        return deps
    return list(set(global_deps))

    