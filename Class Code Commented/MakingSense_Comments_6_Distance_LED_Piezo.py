from gpiozero import LED, Button, DistanceSensor      # Imports the LED, Button, and DistanceSensor functions from the GPIO library
from time import sleep                                # Imports the sleep functions from the time library

led = LED(21)       # Initializes pin 21 as an LED and defines variable name "led"
piezo = LED(12)     # Initializes pin 12 as an LED and defines variable name "piezo", we'll use the LED functions to run our piezo

''' ### Turning a piezo on and off with a capacitive touch button ###
button = Button(16)

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
    
distanceMeters = DistanceSensor(trigger = 8, echo = 11, threshold_distance = 0.15)
# Initializes pins 8 and 11 as a DistanceSensor echo and trigger, respectively, with variable name "distanceMeters". Also sets threshold distance to 0.15m (~6in)
 
while True:                                              # Run the indented code forever
    distanceInches = distanceMeters.distance * 39.37     # Define variable "distanceInches" as distanceMeters times 39.37
    distanceInches = round(distanceInches, 1)            # Define new value of distanceInches as previous value of distanceInches rounded to one decimal place
    
    print('Distance: ', distanceInches, 'in')            # Prints "Distance: XX.X in."
    
    distanceMeters.when_in_range = led.on                # When distance sensed is less than threshold distance, turn on led
    distanceMeters.when_out_of_range = led.off           # When distance sensed is greater than threshold distance, turn off led
    
    if distanceInches <= 3:     # If distance is less than or equals to 3 inches, run the indented code below, otherwise skip to the indented code below else
        piezo.on()              # Turn piezo on
    else:                       # If if statement is not satisfied, run the indented code below
        piezo.off()             # Turn piezo off
        
    sleep(.1)                   # Waits 0.1 seconds before running next line of code, in this case back to initializing distanceInches
