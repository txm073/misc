import re
from urllib.request import urlopen
import importlib
import os, sys

def standard_libs(version=None, top_level_only=True):
    if version is None:
        version = sys.version_info
        version = f"{version.major}.{version.minor}"
    url = f"https://docs.python.org/{version}/py-modindex.html"
    with urlopen(url) as f:
        page = f.read()
    modules = set()
    for module in re.findall(r'#module-(.*?)[\'"]', page.decode('ascii', 'replace')):
        if top_level_only:
            module = module.split(".")[0]
        modules.add(module)
    for module in sys.builtin_module_names:
        modules.add(module)
    return modules

windows_stdlib = []
stdlib = standard_libs(top_level_only=False)
for lib in stdlib:
    try:
        importlib.import_module(lib)
        windows_stdlib.append(lib)
    except ImportError:
        pass
std_namespace = [importlib.import_module(lib) for lib in windows_stdlib]

def recursive_dir(obj, exclude_dunders=True):
    attrs = {attr: getattr(obj, attr) for attr in dir(obj) if attr.startswith("_") and exclude_dunders}
    return 

print(recursive_dir(os))