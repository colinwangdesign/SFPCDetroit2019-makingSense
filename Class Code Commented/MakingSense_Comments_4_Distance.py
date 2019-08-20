from gpiozero import LED, Button, DistanceSensor     # Imports the LED, Button, and DistanceSensor functions from the GPIO library
from time import sleep                               # Imports the sleep functions from the time library

''' ### Initializing pin 21 as an LED with variable name "led" ###
led = LED(21)
'''

''' ### Turning a piezo on and off with a capacitive touch button ###
button = Button(16)
piezo = LED(12)

button.when_pressed = piezo.off
button.when_released = piezo.on
'''

''' ### Turning an led on and off with an if-else statement ###
while True:
    if button.is_pressed:
        led.off()
    else:
        led.on()
'''

distanceMeters = DistanceSensor(trigger = 8, echo = 11)     # Initializes pins 8 and 11 as a DistanceSensor echo and trigger, respectively, and defines variable name "distanceMeters"
 
while True:                                                 # Run the indented code forever
    distanceInches = distanceMeters.distance * 39.37        # Define variable "distanceInches" as distanceMeters times 39.37
    distanceInches = round(distanceInches, 1)               # Define new value of distanceInches as previous value of distanceInches rounded to one decimal place
    
    print('Distance: ', distanceInches, 'in')               # Prints "Distance: XX.X in."
    
    sleep(.1)                                               # Waits 0.1 seconds before running next line of code, in this case back to initializing distanceInches
