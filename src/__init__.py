# save_as_get_screen_size.py
import pyautogui

# This gets the size of the PRIMARY monitor
width, height = pyautogui.size()

print(f"Primary screen size: Width={width}, Height={height}")
