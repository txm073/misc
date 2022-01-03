import pyautogui
import keyboard
import win32gui
import pyperclip

while True:
    if keyboard.is_pressed("ctrl+space"):
        sc = pyautogui.screenshot()
        pixel = sc.getpixel(win32gui.GetCursorPos())
        pyperclip.copy(str(pixel))