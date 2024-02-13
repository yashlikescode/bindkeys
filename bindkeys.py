#from pynput import keyboard
#import time
# Create a keyboard controller
#keyboard_controller = keyboard.Controller()
## Variable to track whether the program should exit
#should_exit = False
print("testing the build")
# Define a function to be called when a key is pressed
'''
def on_key_press(key):
    global should_exit

    if key == keyboard.Key.insert:
        # Press the Windows key and '4' key together - Chrome
        keyboard_controller.press(keyboard.Key.cmd_l)
        keyboard_controller.press('4')
        keyboard_controller.release('4')
        keyboard_controller.release(keyboard.Key.cmd_l)
    elif key == keyboard.Key.scroll_lock:
        keyboard_controller.press(keyboard.Key.cmd_l)
        keyboard_controller.press('5') # Whatsapp
        keyboard_controller.release('5')
        keyboard_controller.release(keyboard.Key.cmd_l)
    elif key == keyboard.Key.pause:
        keyboard_controller.press(keyboard.Key.cmd_l)
        keyboard_controller.press('6') #vs-code
        keyboard_controller.release('6')
        keyboard_controller.release(keyboard.Key.cmd_l)
    elif key == keyboard.Key.esc:
        # Set the exit flag to True
        should_exit = True
        exit()


# Create a listener that listens for key events
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
'''
