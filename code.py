from time import monotonic
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


button2 = digitalio.DigitalInOut(board.GP1)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button_last_press = monotonic()
button2_last_press = monotonic()


kbd = Keyboard(usb_hid.devices)


while True:
    if button.value == True and (monotonic() - button_last_press) > 0.2:
        button_last_press = monotonic()
        led.value = not led.value
        kbd.send(Keycode.SHIFT, Keycode.A)
        print("HELLO")

    elif button2.value == True and (monotonic() - button2_last_press) > 0.2:
        button2_last_press = monotonic()
        kbd.send(Keycode.SHIFT, Keycode.B)
        
