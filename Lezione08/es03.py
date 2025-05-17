import pyautogui

screen_width, screen_height = pyautogui.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y, duration=1)
pyautogui.click()