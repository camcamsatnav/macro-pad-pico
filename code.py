from button import Button
import board
import digitalio


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

buttons = []
bindings = []

f = open("bindings.txt", "r")
f.readline()#ignored as is info line
line = f.readline()

while len(line.strip()) != 0:
    print(line)
    bindings.append(line.strip())
    line = f.readline()

for i in range(len(bindings)):
    buttons.append(Button(i, bindings[i]))

while True:
    for btn in buttons:
        if btn.is_pressed():
            btn.send()
