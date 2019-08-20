from gpiozero import LED, Button, DistanceSensor
from time import sleep

distanceMeters = DistanceSensor(trigger = 8, echo = 11)

while True:
    distanceInches = distanceMeters.distance * 39.37
    distanceInches = round(distanceInches, 1)
    
    print('Distance: ', distanceInches, 'in')
    
    sleep(.1)
