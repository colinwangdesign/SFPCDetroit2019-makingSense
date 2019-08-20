from gpiozero import LED     # Imports the LED functions from the GPIO library
from time import sleep       # Imports the sleep functions from the time library

led = LED(21)    # Initializes pin 21 as an LED and defines variable name "led"

while True:      # Run the indented code forever
    led.on()     # Turns "led" on
    sleep(.5)    # Waits 0.5 seconds before next line of code
    led.off()    # Turns "led" off
    sleep(.5)    # Waits 0.5 seconds before next line of code, in this case back to led.on()