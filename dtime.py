from datetime import datetime
from builtins import print as _print

GLOBAL_DEBUG = False
LOG_PATH = ".log"

def print(*args, **kwargs):
    if kwargs.get("delay") and isinstance(kwargs["delay"], (int, float)):
        time.sleep(kwargs["delay"])
        kwargs.pop("delay")    
    args = str(kwargs.get("sep", " ")).join([str(arg) for arg in args])
    if not GLOBAL_DEBUG:
        if "\n" not in args:
            args = datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]") + " " + args
        else:
            args = datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]") + ":\n" + args + "\n"
        kwargs["file"] = open(LOG_PATH, "a")
    _print(args, **kwargs)

print("Hello there!")