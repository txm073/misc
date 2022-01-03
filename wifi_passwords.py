import subprocess
import sys


def get_password(ssid):
    info = subprocess.run(
        ["netsh", "wlan", "show", "profiles", ssid ,"key=clear"], 
        capture_output=True, text=True, shell=True
    )
    lines = info.stdout.split("\n")
    for l in lines:
        if "Key Content" in l:
            return l[l.index(":") + 1:].strip()

def get_profiles():
    info = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], 
        capture_output=True, text=True, shell=True
    )
    lines = info.stdout.split("\n")
    return [l[l.index(":") + 1:].strip() for l in lines if ":" in l][1:]

def pipe(fn, filename):
    def wrapper(*args, **kwargs):
        pass

def main():
    for i in {ssid: get_password(ssid) for ssid in get_profiles()}.items():
        print("Network:", i[0] + " " * (30 - len(i[0])) + "Password:", i[1])


if __name__ == "__main__":
    main()