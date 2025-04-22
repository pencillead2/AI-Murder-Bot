import time
import os
import glob
from obswebsocket import obsws, requests

timeToDie = 0
timeToDie = str(timeToDie)

# OBS WebSocket Connection Settings
OBS_HOST = "localhost"
OBS_PORT = 4455  # Default WebSocket port for OBS 28+
OBS_PASSWORD = "Finneroo123!"  # Set your OBS WebSocket password

# Manually set the OBS recording directory (update this to your actual path)
MANUAL_RECORDING_PATH = r"C:\Users\price\OneDrive\Desktop\ai death robot\recordings"  # Example path

# New filename
NEW_FILENAME = timeToDie + ".mp4"

# Connect to OBS WebSocket
def connectSocket(OBS_HOST, OBS_PORT, OBS_PASSWORD):
    try:
        ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)
        ws.connect()
        print("Connected to OBS WebSocket.")
        return ws
    except Exception as e:
        print(f"Failed to connect to OBS WebSocket: {e}")
        exit()

# Start Recording
def startRecording(ws):
    try:
        ws.call(requests.StartRecord())
        print("Recording started...")
    except Exception as e:
        print(f"Error starting recording: {e}")
        ws.disconnect()
        exit()

# Allow recording for 5 seconds (adjust as needed)

# Stop Recording
def stopRecording(ws):
    try:
        ws.call(requests.StopRecord())
        print("Recording stopped.")
    except Exception as e:
        print(f"Error stopping recording: {e}")
        ws.disconnect()
        exit()

# Wait a few seconds for OBS to finalize the file

# Find the most recent recording file
def renameFile(ws, MANUAL_RECORDING_PATH, NEW_FILENAME):
    try:
        recordings = sorted(glob.glob(os.path.join(MANUAL_RECORDING_PATH, "*.*")), key=os.path.getmtime, reverse=True)

        if not recordings:
            print("Error: No recording file found.")
            ws.disconnect()
            exit()

        latest_recording = recordings[0]
        new_path = os.path.join(MANUAL_RECORDING_PATH, NEW_FILENAME)

        # Attempt to rename the file
        try:
            os.rename(latest_recording, new_path)
            print(f"Recording renamed to: {new_path}")
        except Exception as e:
            print(f"Error renaming file: {e}")
    except Exception as e:
        print(f"Error finding the latest recording file: {e}")

# Disconnect from OBS
def disconnectSocket(ws):
    ws.disconnect()
    print("Disconnected from OBS.")

"""

im assuming we have so place we store the death times and we can access it
also assuming timetodie will already be put in the array before this code is run

if timeToDie = min(arrayOfTimes):
    rename file
else:
    delete file
"""