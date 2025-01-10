# Created by Abzikel
import time
import random
from keyboard import press_and_release_key

# Auto Hunting
def auto_hunting(settings, stop_event, running_window):
    try:
        active_settings = settings["autoHunting"]

        # Initialize last execution times for each active action
        last_execution_times = {
            key: 0 for key, value in active_settings.items() if isinstance(value, dict) and value.get("active")
        }
        last_auto_picking_time = 0  # Separate variable for Auto Picking

        # Initial 5-second delay before starting the bot
        print("Starting bot in 5 seconds...")
        time.sleep(5)

        # Main bot loop
        while not stop_event.is_set():
            current_time = time.time()  # Current timestamp in seconds

            # Process each active key
            for key, value in active_settings.items():
                if isinstance(value, dict) and value.get("active"):
                    key_to_press = value["text"]
                    delay = value["delay"]

                    # Determine the delay (random or fixed)
                    if "-" in delay:
                        min_delay, max_delay = map(int, delay.split("-"))
                        wait_time = random.randint(min_delay, max_delay) / 1000  # Convert to seconds
                    else:
                        wait_time = int(delay) / 1000  # Convert to seconds

                    # Check if the key is ready to be pressed
                    if current_time - last_execution_times[key] >= wait_time:
                        press_and_release_key(key_to_press)
                        print(f"Pressed {key_to_press}, next in {wait_time} seconds")
                        time.sleep(1)
                        last_execution_times[key] = current_time

            # Auto Picking logic
            if active_settings.get("autoPicking"):
                auto_picking_delay = active_settings.get("autoPickingDelay", "500")
                if "-" in auto_picking_delay:
                    min_delay, max_delay = map(int, auto_picking_delay.split("-"))
                    wait_time = random.randint(min_delay, max_delay) / 1000
                else:
                    wait_time = int(auto_picking_delay) / 1000

                # Check if Auto Picking is ready to execute
                if current_time - last_auto_picking_time >= wait_time:
                    press_and_release_key("z")
                    print(f"Pressed Z (Auto Picking), next in {wait_time} seconds")
                    last_auto_picking_time = current_time

            # Small delay to avoid high CPU usage
            time.sleep(0.01)
    except Exception as e:
        print(f"Error in bot: {e}")
    finally:
        stop_event.set()  # Ensure the stop event is set in case of failure
