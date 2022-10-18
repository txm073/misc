import ctypes
import time

time.sleep(3)
print(ctypes.windll.user32.SetCursorPos(100, 200))
print(ctypes.windll.kernel32.GetLastError())