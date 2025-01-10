# Created by Abzikel
import os
import json

# Function to initialize the settings file
def initialize_settings_file():
    # If the file doesn't exists create it
    if not os.path.exists("settings.txt"):
        # Create default settings
        default_settings = {
            "autoHunting": {
                "potion1": {"text": "F1", "active": False, "delay": "400-600"},
                "potion2": {"text": "F2", "active": False, "delay": "10000-15000"},
                "potion3": {"text": "F3", "active": False, "delay": "601000"},
                "potion4": {"text": "F4", "active": False, "delay": "601000"},
                "skill1": {"text": "1", "active": False, "delay": "12000"},
                "skill2": {"text": "2", "active": False, "delay": "12000"},
                "autoPicking": True,
                "autoPickingDelay": "600-800"
            }
        }

        # Create file and save it as "settings.txt"
        with open("settings.txt", "w") as file:
            json.dump(default_settings, file, indent=4)
        print("Default settings file created.")

# Function to load settings from the file
def load_settings():
    initialize_settings_file()
    with open("settings.txt", "r") as file:
        return json.load(file)

# Function to save settings to the file
def save_settings(auto_hunting_settings):
    with open("settings.txt", "w") as file:
        json.dump({"autoHunting": auto_hunting_settings}, file, indent=4)
