from gpiozero import LED, Button     # Imports the LED and Button functions from the GPIO library
from time import sleep               # Imports the sleep functions from the time library

led = LED(21)           # Initializes pin 21 as an LED and defines variable name "led"
button = Button(16)     # Initializes pin 16 as a Button and defines variable name "button"

button.when_pressed = led.off     # When button pin value goes high, turn led off
button.when_released = led.on     # When button pin value goes low, turn led on *See comment below about why this seems backwards

''' ### Turning an led on and off with an if-else statement ###
while True:
    if button.is_pressed:
        led.off()
    else:
        led.on() '''

''' ***Explanation of capacitive touch sensors and why they are backwards from how a regular push button works***

Capactive touch sensors output high to the signal pin when untouched (the circuit is closed and complete).
When touched, the circuit is grounded by your finger, and the button outputs low to the signal pin
(the circuit is open and incomplete). This is the opposite of how a regular passive push button works,
where when pushed down the circuit is physically closed and completed,
and allows a high signal to travel through to the signal pin.
'''
