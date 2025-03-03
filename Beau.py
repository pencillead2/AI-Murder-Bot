import pyautogui
import keyboard
import time

# Hold 'w' for 5 seconds
time.sleep(5)
keyboard.press('w')
time.sleep(2)
keyboard.release('w')

# Press spacebar twice with a 5-second gap
keyboard.press('space')
time.sleep(.25)
keyboard.release('space')
time.sleep(2)
keyboard.press('space')
time.sleep(.25)
keyboard.release('space')

# Move the mouse up
pyautogui.move(0, -500, duration=1)  # Move the mouse 100 pixels up

