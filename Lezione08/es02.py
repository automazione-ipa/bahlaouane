import pyautogui
import time
import subprocess 

pyautogui.hotkey('win', 's')
time.sleep(1)
pyautogui.write("Outlook")
pyautogui.press('enter')
time.sleep(5)  

pyautogui.write("Ciao mondo!")
pyautogui.hotkey('ctrl', 's')
time.sleep(2)

pyautogui.write("ciao.txt")
time.sleep(2)
pyautogui.press('enter')