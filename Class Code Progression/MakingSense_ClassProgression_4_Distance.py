from gpiozero import LED, Button, DistanceSensor
from time import sleep

#led = LED(21)
#piezo = LED(12)
#button = Button(16)
#
#button.when_pressed = piezo.off
#button.when_released = piezo.on

#while True:
#    if button.is_pressed:
#        led.off()
#    else:
#        led.on()

distanceMeters = DistanceSensor(trigger = 18, echo = 14)

while True:
    distanceInches = distanceMeters.distance * 39.37
    distanceInches = round(distanceInches, 1)
    
    print('Distance: ', distanceInches, 'in')
    
    sleep(.1)