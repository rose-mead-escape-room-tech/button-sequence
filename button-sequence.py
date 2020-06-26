
from time import sleep                  
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
import collections

sequenceRequired = "05873"              # correct combo  
sequence = collections.deque(maxlen=5)  # variable to store combo as buttons are pressed
digitPressed = ()

chan_list = [2,3,4,14,15,18,23,25,8,7]

GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(chan_list, GPIO.FALLING, callback=saveButtonPress, bouncetime=10000) 

def saveButtonPress(channel):
    global digitPressed
    global sequence
    digitPressed = chan_list.index(channel)
    sequence.append(digitPressed)

def solved():
    sleep(14)
    # Do something here
    
def mainRoutine():
    global sequence
    global sequenceRequired
        return
    sleep(0.10000)

    sequencestring = (''.join(map(str,sequence)))
    if sequencestring == sequenceRequired:
        solved()


while(True):
    mainRoutine()

        
