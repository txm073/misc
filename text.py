import os, sys

def tree(directory=os.path.abspath(os.path.dirname(__file__)), 
        display=True, filter=False, sort=True, pipe=None, return_items=True, rlevel=0):
    if rlevel == 0:
        global global_items 
        global_items = []
        if pipe:
            with open(pipe, "w") as f:
                pass

    items = sorted(os.listdir(directory)) if sort else os.listdir(directory)
    if filter:
        items = [item for item in items if item.lower() not in [".git", "__pycache__"] 
                    or "ignore" in item.lower() or "cache" in item.lower()]
    for item in items:
        subdir = os.path.isdir(os.path.join(directory, item))
        string = "+" + "-" * (rlevel * 3) + " " + item
        if subdir:
            string += ":"
        if display:
            print(string if rlevel != 0 else item + (":" if subdir else ""), 
                    file=open(pipe, "a") if pipe else sys.stdout)
        if subdir:
            tree(os.path.join(directory, item), display=display, 
                        filter=filter, sort=sort, rlevel=rlevel+1)
        global_items.append(os.path.join(directory, item))
    if rlevel == 0 and return_items:
        return global_items    
    
items = tree("E:\\Python", filter=True, pipe="output.txt")

