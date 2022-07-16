import os, sys
import subprocess
from win32com.shell import shell

def _execute(cmd, *args, **kwargs):
    response = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, text=True, shell=True)
    return response.stdout

def _open(program):
    subprocess.Popen(program, shell=True)

def close(program):
    _execute(f'TASKKILL /F /IM {os.path.basename(program)}')

def running(sort="name"):
    processes = []
    output = _execute("tasklist")
    for line in output.split("\n")[3:-1]:
        elements = [elem.strip() for elem in line.split("  ") if elem != ""]
        del elements[1:-1]
        processes.append(elements)    
    if sort == "name":
        return sorted(processes, key=lambda e: e[0].lower())
    return sorted(processes, key=lambda e: int(e[1].split(" ")[0].replace(",", "")))

def run_elevated(terminal="powershell.exe", command=None):
    shell.ShellExecuteEx(lpVerb="runas", lpFile=terminal, lpParameters=command)


