# electronic rainbow

from machine import Pin
from time import sleep

LED = [25, 33, 32]

del_time = 0.5

for i in range(3):
    LED[i] = Pin(LED[i], Pin.OUT)

while True:
    for i in range(3):
        LED[i].value(1)
        sleep(del_time)
        LED[i].value(0)

