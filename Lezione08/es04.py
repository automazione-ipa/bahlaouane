import pyautogui
import pyperclip
import time

pyautogui.hotkey('win', 's')
time.sleep(1)
pyautogui.write("Outlook")
pyautogui.press('enter')
time.sleep(5)  

pyautogui.hotkey('ctrl', 'n')
time.sleep(2)

pyperclip.copy("l.salzone@alfasoft.it")
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('tab') # to tab 
pyautogui.press('tab') # cc tab 
pyautogui.press('tab')

pyautogui.write("Test invio automatico")
pyautogui.press('tab') 

time.sleep(2)
pyautogui.write("Ciao,\n\nQuesto è un messaggio inviato automaticamente con Python.")

time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')
pyautogui.hotkey('enter')

print("Email inviata con successo!")