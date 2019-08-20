from gpiozero import LED, Button     # Imports the LED and Button functions from the GPIO library
from time import sleep               # Imports the sleep functions from the time library

led = LED(21)           # Initializes pin 21 as an LED and defines variable name "led"
button = Button(16)     # Initializes pin 16 as a Button and defines variable name "button"
piezo = LED(12)         # Initializes pin 12 as an LED and defines variable name "piezo", we'll use the LED functions to run our piezo

button.when_pressed = piezo.off     # When button pin value goes high, turn led off
button.when_released = piezo.on     # When button pin value goes low, turn led on *See comment below about why this seems backwards

''' ### Turning an led on and off with an if-else statement ###
while True:
    if button.is_pressed:
        led.off()
    else:
        led.on()
'''