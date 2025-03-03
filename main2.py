from screenToRgb import screen_to_rgb
from recordingTest import connectSocket, startRecording, stopRecording, renameFile, disconnectSocket
import numpy as np
import pyautogui
import keyboard
import time

alive = True

weight0 = np.random.uniform(-1.0, 1.0, (100,691200)) 
weight1 = np.random.uniform(-1.0, 1.0, (100,100)) 
weight2 = np.random.uniform(-1.0, 1.0, (100,100)) 
weight3 = np.random.uniform(-1.0, 1.0, (12,100)) 
weights = [weight0, weight1, weight2, weight3] 

bias0 = np.random.uniform(-1.0, 1.0, 100) #I believe this might need to be np.random.random
bias1 = np.random.uniform(-1.0, 1.0, 100) 
bias2 = np.random.uniform(-1.0, 1.0, 100) 
bias3 = np.random.uniform(-1.0, 1.0, 12) #12 controls: W, A, S, D, spacebar, Mouse up, down, left, right, LShift, Lclick, Rclick 
biases = [bias0, bias1, bias2, bias3] 

OBS_HOST = "localhost"
OBS_PORT = 4455  # Default WebSocket port for OBS 28+
OBS_PASSWORD = "password123"  # Set your OBS WebSocket password

MANUAL_RECORDING_PATH = r"C:\Users\Tech Lab\Desktop\sean\AI Murder Bot (DO NOT RUN)\videos"  # Example path

def pressW(holdDown):
    if holdDown:
        pyautogui.keyDown('w')
    else:
        pyautogui.keyUp('w')

def pressA(holdDown):
    if holdDown:
        pyautogui.keyDown('a')
    else:
        pyautogui.keyUp('a')

def pressS(holdDown):
    if holdDown:
        pyautogui.keyDown('s')
    else:
        pyautogui.keyUp('s')

def pressD(holdDown):
    if holdDown:
        pyautogui.keyDown('d')
    else:
        pyautogui.keyUp('d')

def pressShift(holdDown):
    if holdDown:
        pyautogui.keyDown('shift')
    else:
        pyautogui.keyUp('shift')

def pressSpacebar(holdDown):
    if holdDown:
        pyautogui.keyDown('space')
    else:
        pyautogui.keyUp('space')

def leftMouseButton(holdDown):
    if holdDown:
        pyautogui.mouseDown(button='left')
    else:
        pyautogui.mouseUp(button='left')

def rightMouseButton(holdDown):
    if holdDown:
        pyautogui.mouseDown(button='right')
    else:
        pyautogui.mouseUp(button='right')

def mouseUp(holdDown): #these might be wrong
    if holdDown:
        pyautogui.move(0, -100)

def mouseDown(holdDown):
    if holdDown:
        pyautogui.move(0, 100)

def mouseLeft(holdDown):
    if holdDown:
        pyautogui.move(-100, 0)

def mouseRight(holdDown):
    if holdDown:
        pyautogui.move(100, 0, duration=0.05)

controls = [pressW, pressA, pressS, pressD, pressShift, pressSpacebar, mouseUp, mouseDown, mouseLeft, mouseRight, leftMouseButton, rightMouseButton]

def normalizeFunc(number): 
    return max(min(number + 0.5, 1), 0) 

startTime = time.time()
ws = connectSocket(OBS_HOST, OBS_PORT, OBS_PASSWORD)
startRecording(ws)

time.sleep(3)

while alive:
    if keyboard.is_pressed('k'):
        alive = False

    data = np.array(screen_to_rgb()).flatten() / 256.0

    for i in range(4): 
        #data = normalizeFunc(weights[i]@data+biases[i]) #data = normalizeFunc(np.dot(weights[i], data) + biases[i])
        data = np.array(list(map(lambda x: normalizeFunc(x), weights[i]@data+biases[i])))
        print(data)
        print(np.shape(data))

    for i in range(len(data)):
        if data[i] > 0.5:
            controls[i](True) #do that thing if output is greater than 0.5 
        else:
            controls[i](False)

timeToDie = time.time()-startTime
print(timeToDie)

# New filename
NEW_FILENAME = str(timeToDie) + ".mp4"

stopRecording(ws)
time.sleep(5)
renameFile(ws, MANUAL_RECORDING_PATH, NEW_FILENAME)
disconnectSocket(ws)