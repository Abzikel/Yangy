# Created by Abzikel
import tkinter as tk
import threading
from bot import auto_hunting
from config import load_settings, save_settings

# Function to open the main window
def open_main_window(current_window):
    # Close the current window
    current_window.destroy()
    
    # Recreate the main window
    root = tk.Tk()
    root.title("Yangy - Metin2 Bot")
    root.geometry("300x300")

    # Create a frame to center the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    # Auto Hunting Button
    auto_hunting_button = tk.Button(button_frame, text="Auto hunting", width=15, command=lambda: open_auto_hunting_window(root))
    auto_hunting_button.pack(pady=10)

    # Fragments Button
    auto_hunting_button = tk.Button(button_frame, text="Fragments", width=15)
    auto_hunting_button.pack(pady=10)

    # Run the main window
    root.mainloop()
        
# Function to open the Auto Hunting window
def open_auto_hunting_window(current_window):
    # Close the current window
    current_window.destroy()
    
    # Create the Auto Hunting window
    auto_hunting_window = tk.Tk()
    auto_hunting_window.title("Yangy - Auto Hunting")
    auto_hunting_window.geometry("300x300")

    # Create a frame to center the buttons
    button_frame = tk.Frame(auto_hunting_window)
    button_frame.pack(expand=True)

    # Start Button
    start_button = tk.Button(button_frame, text="Start", width=15, command=lambda: open_auto_hunting_running_window(auto_hunting_window))
    start_button.pack(pady=10)

    # Settings Button
    settings_button = tk.Button(button_frame, text="Settings", width=15, command=lambda: open_auto_hunting_settings_window(auto_hunting_window))
    settings_button.pack(pady=10)

    # Back Button
    back_button = tk.Button(button_frame, text="Back", width=15, command=lambda: open_main_window(auto_hunting_window))
    back_button.pack(pady=10)

    # Run the Auto Hunting window
    auto_hunting_window.mainloop()
    
# Function to open the bot running window
def open_auto_hunting_running_window(current_window):
    # Close the current window
    current_window.destroy()
    
    # Load settings
    settings = load_settings()

    # Create the Bot Running window
    running_window = tk.Tk()
    running_window.title("Yangy - Auto Hunting Running...")
    running_window.geometry("300x150")

    # Create a frame for the Stop button
    button_frame = tk.Frame(running_window)
    button_frame.pack(expand=True)

    # Stop event for the bot
    stop_event = threading.Event()

    # Start the bot in a separate thread
    bot_thread = threading.Thread(target=auto_hunting, args=(settings, stop_event, running_window))
    bot_thread.start()

    # Function to stop the bot and return to the Auto Hunting window
    def stop_and_return():
        stop_event.set()  # Signal to stop the bot
        open_auto_hunting_window(running_window)  # Reopen the Auto Hunting window

    # Stop Button
    stop_button = tk.Button(button_frame, text="Stop", width=15, command=stop_and_return)
    stop_button.pack(pady=20)

    # Run the Bot Running window
    running_window.mainloop()
    stop_event.set()  # Ensure the thread is stopped when the window is closed

def open_auto_hunting_settings_window(current_window):
    # Close the current window
    current_window.destroy()
    
    # Load settings
    settings = load_settings()["autoHunting"]

    # Create the Auto Hunting Settings window
    auto_hunting_settings_window = tk.Tk()
    auto_hunting_settings_window.title("Yangy - Auto Hunting Settings")
    auto_hunting_settings_window.geometry("600x500")

    # Create a frame for organizing the elements
    frame = tk.Frame(auto_hunting_settings_window)
    frame.pack(pady=20, padx=20)

    # Add header row for information
    header_frame = tk.Frame(frame)
    header_frame.pack(fill="x", pady=10)

    # Header labels
    tk.Label(header_frame, text="Usage", width=12, anchor="w").pack(side="left", padx=5)
    tk.Label(header_frame, text="Key", width=5, anchor="w").pack(side="left", padx=5)
    tk.Label(header_frame, text="Delay", width=15, anchor="w").pack(side="left", padx=5)
    tk.Label(header_frame, text="ms", width=5, anchor="w").pack(side="left", padx=5)
    tk.Label(header_frame, text="Is Active?", width=10, anchor="w").pack(side="right", padx=5)

    # Variables to store widget bindings
    potion_vars = []
    skill_vars = []
    auto_picking_var = tk.BooleanVar(value=settings["autoPicking"])
    auto_picking_delay_var = tk.StringVar(value=settings.get("autoPickingDelay", "500"))

    # Loop to create Potion inputs, checkboxes, and delay fields
    for index in range(1, 5):  # Potion 1 to Potion 4
        potion_frame = tk.Frame(frame)
        potion_frame.pack(fill='x', pady=5)

        # Label for Potion
        potion_label = tk.Label(potion_frame, text=f"Potion {index}:", width=12, anchor="w")
        potion_label.pack(side="left", padx=5)

        # Entry for Potion
        potion_var = tk.StringVar(value=settings[f"potion{index}"]["text"])
        potion_entry = tk.Entry(potion_frame, width=5, textvariable=potion_var)
        potion_entry.pack(side="left", padx=5)

        # Delay Field for Potion
        delay_var = tk.StringVar(value=settings[f"potion{index}"]["delay"])
        delay_entry = tk.Entry(potion_frame, width=15, textvariable=delay_var)
        delay_entry.pack(side="left", padx=5)

        delay_label = tk.Label(potion_frame, text="ms", anchor="w", width=5)
        delay_label.pack(side="left")

        # Checkbox for Potion
        potion_active_var = tk.BooleanVar(value=settings[f"potion{index}"]["active"])
        potion_checkbox = tk.Checkbutton(potion_frame, variable=potion_active_var)
        potion_checkbox.pack(side="right", padx=5)
        potion_vars.append((potion_var, delay_var, potion_active_var))

    # Loop to create Skill inputs, checkboxes, and delay fields
    for index in range(1, 3):  # Skill 1 to Skill 2
        skill_frame = tk.Frame(frame)
        skill_frame.pack(fill='x', pady=5)

        # Label for Skill
        skill_label = tk.Label(skill_frame, text=f"Skill {index}:", width=12, anchor="w")
        skill_label.pack(side="left", padx=5)

        # Entry for Skill
        skill_var = tk.StringVar(value=settings[f"skill{index}"]["text"])
        skill_entry = tk.Entry(skill_frame, width=5, textvariable=skill_var)
        skill_entry.pack(side="left", padx=5)

        # Delay Field for Skill
        delay_var = tk.StringVar(value=settings[f"skill{index}"]["delay"])
        delay_entry = tk.Entry(skill_frame, width=15, textvariable=delay_var)
        delay_entry.pack(side="left", padx=5)

        delay_label = tk.Label(skill_frame, text="ms", anchor="w", width=5)
        delay_label.pack(side="left")

        # Checkbox for Skill
        skill_active_var = tk.BooleanVar(value=settings[f"skill{index}"]["active"])
        skill_checkbox = tk.Checkbutton(skill_frame, variable=skill_active_var)
        skill_checkbox.pack(side="right", padx=5)
        skill_vars.append((skill_var, delay_var, skill_active_var))

    # Auto Picking Checkbox with Delay Field
    auto_picking_frame = tk.Frame(frame)
    auto_picking_frame.pack(fill='x', pady=10)

    auto_picking_label = tk.Label(auto_picking_frame, text="Auto Picking:", width=12, anchor="w")
    auto_picking_label.pack(side="left", padx=5)
    
    invisible_spacer = tk.Entry(auto_picking_frame, width=5, state="disabled")  # Invisible entry
    invisible_spacer.pack(side="left", padx=5)

    auto_picking_delay_entry = tk.Entry(auto_picking_frame, width=15, textvariable=auto_picking_delay_var)
    auto_picking_delay_entry.pack(side="left", padx=5)

    delay_label = tk.Label(auto_picking_frame, text="ms", anchor="w", width=5)
    delay_label.pack(side="left")

    auto_picking_checkbox = tk.Checkbutton(auto_picking_frame, variable=auto_picking_var)
    auto_picking_checkbox.pack(side="right", padx=5)

    # Function to save settings and go back
    def save_and_back():
        # Save the updated settings
        updated_settings = {
            f"potion{index}": {
                "text": potion_vars[index - 1][0].get().upper(),
                "delay": potion_vars[index - 1][1].get(),
                "active": potion_vars[index - 1][2].get()
            }
            for index in range(1, 5)
        }
        updated_settings.update({
            f"skill{index}": {
                "text": skill_vars[index - 1][0].get().upper(),
                "delay": skill_vars[index - 1][1].get(),
                "active": skill_vars[index - 1][2].get()
            }
            for index in range(1, 3)
        })
        updated_settings["autoPicking"] = auto_picking_var.get()
        updated_settings["autoPickingDelay"] = auto_picking_delay_var.get()

        save_settings(updated_settings)
        open_auto_hunting_window(auto_hunting_settings_window)

    # Back Button
    back_button = tk.Button(auto_hunting_settings_window, text="Back", width=15, command=save_and_back)
    back_button.pack(pady=20)

    # Run the Settings window
    auto_hunting_settings_window.mainloop()