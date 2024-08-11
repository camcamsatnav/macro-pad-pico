from digitalio import DigitalInOut, Direction, Pull
from time import monotonic
import board
from usb_hid import devices
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from microcontroller import Pin

class Button:

    kbd = Keyboard(devices)

    def __init__(self, pin: int, binding: str) -> None:
        self.pin = pin
        self.button = DigitalInOut(Button.get_pin(pin))
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.DOWN
        self.binding = binding
        self.last_press = monotonic()


    def is_pressed(self) -> bool:
        if self.button.value == True and (monotonic() - self.last_press) > 0.2:
            self.last_press = monotonic()
            return True
        return False
    
    def send(self) -> None:
        Button.kbd.send(*[getattr(Keycode, x.upper()) for x in self.binding.split(" + ")])

    @staticmethod
    def get_pin(pin: int) -> Pin:
        return getattr(board, f"GP{pin}")
