from gpiozero import LED, Button

led = LED(24)
button = Button(23)

if button.is_pressed:
    led.on()
else:
    led.off()

    