from gpiozero import LED, Button
from time import sleep

led = LED(21)
piezo = LED(12)
button = Button(16)

button.when_pressed = piezo.off
button.when_released = piezo.on

#while True:
#    if button.is_pressed:
#        led.off()
#    else:
#        led.on()
