
from pynput.keyboard import Listener 
from pynput.keyboard import Key, Controller
import logging 



logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

keyboard = Controller()

def show(key): 

    print('\nYou entered {0}'.format( key))

    if key == Key.esc:
        return False
    
    with Listener(on_press = show) as listener: 
        listener.join()


#with Listener(on_press = on_press, on_release = on_release) as listener: 
#listener.join()


def on_press(key): 
    if key == Key.esc: 
        return False
    logging.info("pressed{0}".format(key))

def on_release(key): 
    logging.info("released {0}".format(key))
#input_user = str(input('y/n'))
 
#listener =  Listener(on_press = on_press, on_release = on_release)
##listener.start()
#listener.join()
show(Key)
