
import keyboard
import pyperclip
import threading
import random
import time

emojis = [
    "😭", "💀", "🙏", "🔥", "🥀", "💔",
    "😂", "🤣", "😈", "🤡", "👹", "👀",
    "🗿", "🥶", "🤯", "😎", "🤓", "😱",
    "🤑", "😡", "🤫", "🫠", "😵", "🤨",
    "😏", "🤖", "👽", "💩", "🙀", "👻"
]

EMOJIS_PER_ROW = 8
PASTE_DELAY = 0.04
ROW_DELAY = 0.15

enabled = threading.Event()
shutdown = threading.Event()

def toggle():
    if enabled.is_set():
        enabled.clear()
        print("OFF")
    else:
        enabled.set()
        print("ON")

def worker():
    while not shutdown.is_set():
        if not enabled.wait(timeout=0.05):
            continue

        row = "".join(random.choices(emojis, k=EMOJIS_PER_ROW))
        pyperclip.copy(row)

        keyboard.send("ctrl+v")
        time.sleep(PASTE_DELAY)

        if enabled.is_set() and not shutdown.is_set():
            keyboard.send("enter")

        time.sleep(ROW_DELAY)

keyboard.add_hotkey("=", toggle, suppress=True)
keyboard.add_hotkey("esc", shutdown.set)

threading.Thread(target=worker, daemon=True).start()

print("= : ON / OFF")
print("ESC : EXIT")

shutdown.wait()
enabled.clear()
keyboard.unhook_all()
