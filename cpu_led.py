from gpiozero import LEDBarGraph, LoadAverage
import random
from time import sleep
from signal import pause

bar = LEDBarGraph(26, 19, 13, 6, 5, pwm=True)
la = LoadAverage(minutes=1, max_load_average=5)

bar.source = la

pause()