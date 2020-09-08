from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=13, trigger=15, max_distance=2.0)

while True:
 distance = sensor.distance * 100
 print("Distance : " , distance)
 sleep(1)