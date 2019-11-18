import RPi.GPIO as GPIO
from time import sleep, gmtime, strftime

strftime("%H:%M:%S", gmtime())  #set time format
GPIO.setmode(GPIO.BCM)  #using broadcom chip's pinouts
GPIO.setup(2, GPIO.OUT) #2 is an output
GPIO.setup(0, GPIO.OUT) #0 isan output


def forward():
    GPIO.output(2, 0)  # set GPIO2 to 0/GPIO.LOW/False
    GPIO.output(0, 1)  # set GPIO0 to 1/GPIO.HIGH/True


def reverse():
    print(gmtime(), "- going backwards")
    GPIO.output(2, 1)  # set GPIO2 to 1/GPIO.HIGH/True
    GPIO.output(0, 0)  # set GPIO0 to 0/GPIO.LOW/False


print(strftime())