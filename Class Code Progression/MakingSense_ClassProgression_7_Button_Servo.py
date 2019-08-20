from gpiozero import LED, Button, DistanceSensor, Servo
from time import sleep

#led = LED(21)
#piezo = LED(12)
button = Button(16)
servo = Servo(8)

#button.when_pressed = piezo.off
#button.when_released = piezo.on

while True:
    
    if button.is_pressed == False:
        servo.max()
    else:
        servo.min()

#while True:
#    if button.is_pressed:
#        led.off()
#    else:
#        led.on()

#distanceMeters = DistanceSensor(trigger = 18, echo = 14, threshold_distance = 0.15)
#
#while True:
#    distanceInches = distanceMeters.distance * 39.37
#    distanceInches = round(distanceInches, 1)
#    
#    print('Distance: ', distanceInches, 'in')
#    
#    distanceMeters.when_in_range = led.on
#    distanceMeters.when_out_of_range = led.off
#
#    if distanceInches <= 3:
#        piezo.on()
#    else:
#        piezo.off()
#        
#    sleep(.1)
