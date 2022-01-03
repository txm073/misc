import os
import subprocess


def create_autostartup():
    os.system('schtasks.exe /create /tn "Python_Startup" /ru SYSTEM /Sc ONSTART /tr "C:\python_startup.bat"')