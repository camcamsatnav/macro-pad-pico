from buttoninit import Button
import board
import digitalio


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

buttons = []
bindings = ["shift + a", "shift + b"]




for i in range(2):
    buttons.append(Button(i, bindings[i]))


# button = digitalio.DigitalInOut(board.GP0)
# button.direction = digitalio.Direction.INPUT
# button.pull = digitalio.Pull.DOWN

# button2 = digitalio.DigitalInOut(board.GP1)
# button2.direction = digitalio.Direction.INPUT
# button2.pull = digitalio.Pull.DOWN





while True:
    for btn in buttons:
        if btn.is_pressed():
            btn.send()
            
    # if button.button.value == True and (monotonic() - button_last_press) > 0.2:
    #     button_last_press = monotonic()
    #     led.value = not led.value
        
    #     print("HELLO")

    # elif button2.button.value == True and (monotonic() - button2_last_press) > 0.2:
    #     button2_last_press = monotonic()
    #     kbd.send(Keycode.SHIFT, Keycode.B)
