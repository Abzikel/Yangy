# Created by Abzikel
from pynput.keyboard import Controller, Key
import time

# Initialize keyboard controller
keyboard = Controller()

# Mapping keys to pynput's Key constants
KEY_MAPPING = {
    "F1": Key.f1,
    "F2": Key.f2,
    "F3": Key.f3,
    "F4": Key.f4,
    "F5": Key.f5,
    "F6": Key.f6,
    "F7": Key.f7,
    "F8": Key.f8,
    "F9": Key.f9,
    "F10": Key.f10,
    "F11": Key.f11,
    "F12": Key.f12,
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "Ñ": "ñ",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
}

# Function to press and release a key
def press_and_release_key(key):
    try:
        # Check if the key is mapped
        mapped_key = KEY_MAPPING.get(key, key)  # Use the key directly if not mapped
        keyboard.press(mapped_key)
        time.sleep(0.05)  # Simulate a short delay for key press
        keyboard.release(mapped_key)
        print(f"Pressed and released: {key}")
    except Exception as e:
        print(f"Error pressing key {key}: {e}")
