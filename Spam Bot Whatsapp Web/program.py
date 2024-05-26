import pyautogui
import webbrowser as wb
import time

wb.open("web.whatsapp.com")
time.sleep(30)

for i in range(1000):
    pyautogui.press("W")
    pyautogui.press("A")
    pyautogui.press("N")
    pyautogui.press("J")
    pyautogui.press("A")
    pyautogui.press("Y")
    pyautogui.press("enter")
    pyautogui.press("B")
    pyautogui.press("R")
    pyautogui.press("O")
    pyautogui.press("enter")
