from gpiozero import LED, Button

led = LED(24)
button = Button(23)
while True:
    print("Testing")
    if button.is_pressed:
        led.on()
    else:
        led.off()

    