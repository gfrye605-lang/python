import keyboard
import pyperclip
import threading
import random
import string
import time

MIN_CHUNK = 250
MAX_CHUNK = 5000

MIN_PASTE_DELAY = 0.04
MAX_PASTE_DELAY = 1.0

MIN_REST = 0.5
MAX_REST = 1.0

enabled = threading.Event()
shutdown = threading.Event()

def toggle():
    if enabled.is_set():
        enabled.clear()
        print("OFF")
    else:
        enabled.set()
        print("ON")

def get_paste_delay(size):
    progress = (size - MIN_CHUNK) / (MAX_CHUNK - MIN_CHUNK)
    return MIN_PASTE_DELAY + progress * (
        MAX_PASTE_DELAY - MIN_PASTE_DELAY
    )

def spam():
    while not shutdown.is_set():
        if not enabled.wait(timeout=0.05):
            continue

        size = random.randint(MIN_CHUNK, MAX_CHUNK)

        chunk = "".join(
            random.choices(string.ascii_letters, k=size)
        )

        paste_delay = get_paste_delay(size)

        pyperclip.copy(chunk)
        keyboard.send("ctrl+v")

        if shutdown.wait(paste_delay):
            break

        if enabled.is_set():
            keyboard.send("enter")
            print(
                f"Sent {size} letters | "
                f"Paste delay: {paste_delay:.2f}s"
            )

        rest = random.uniform(MIN_REST, MAX_REST)
        shutdown.wait(rest)

keyboard.add_hotkey("=", toggle, suppress=True)
keyboard.add_hotkey("esc", shutdown.set)

threading.Thread(target=spam, daemon=True).start()

print("Press = to toggle ON/OFF")
print("Press ESC to exit")

shutdown.wait()
enabled.clear()
keyboard.unhook_all()