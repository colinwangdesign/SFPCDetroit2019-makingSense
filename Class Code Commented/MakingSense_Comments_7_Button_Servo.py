from gpiozero import LED, Button, DistanceSensor, Servo      # Imports the LED, Button, DistanceSensor, and Servo functions from the GPIO library
from time import sleep                                       # Imports the sleep functions from the time library

button = Button(16)     # Initializes pin 16 as a Button and defines variable name "button"
servo = Servo(8)       # Initializes pin 18 as a Servo and defines variable name "servo"

''' ### Commented out code for led and piezo ###
led = LED(21)
piezo = LED(12)

button.when_pressed = piezo.off
button.when_released = piezo.on
'''

while True:                        # Run the indented code forever
    if button.is_pressed == False: # If capactive touch button is touched (False meaning the signal is low run the indented code below, otherwise skip to the indented code below else
        servo.max()                # Turn the servo to its maximum position
    else:                          # If if statement is not satisfied, run the indented code below
        servo.min()                # Turn the servo to its minimum position
        
''' ### Turning an led on and off with an if-else statement ###
while True:
    if button.is_pressed:
        led.off()
    else:
        led.on()
'''

''' ### Distance sensor code ###
distanceMeters = DistanceSensor(trigger = 18, echo = 14, threshold_distance = 0.15)

while True:
    distanceInches = distanceMeters.distance * 39.37
    distanceInches = round(distanceInches, 1)
    
    print('Distance: ', distanceInches, 'in')
    
    distanceMeters.when_in_range = led.on
    distanceMeters.when_out_of_range = led.off

    if distanceInches <= 3:
        piezo.on()
    else:
        piezo.off()
        
    sleep(.1)
'''
