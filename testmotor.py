import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(15,gpio.OUT)

while True:
    gpio.output(15,gpio.HIGH)
    time.sleep(4)
    gpio.output(15,gpio.LOW)
    time.sleep(4)