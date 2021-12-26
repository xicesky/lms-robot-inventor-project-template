# LEGO type:standard slot:0 autostart

from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()


# Write your program here.
#hub.speaker.beep()
#hub.sound.beep()
#print(hub.version)

# for attr, value in hub.__dict__.items():
#     print(attr, value)

#print(hub.__dict__)

# accs = [
#     [57,60,64,67],
#     [60,64,67,71],
#     [64,67,71,74],
#     [65,69,72,76],
# ] 

# motor = Motor('A')
# motor.start_at_power(
#     power=50
# )

# arpeggio = 2.0
# vol = 0
# for _ in range(0, 2):
#     for acc in accs:
#         for iNote in range(0, int(len(acc) * arpeggio)):
#             note = acc[iNote % len(acc)]
#             hub.speaker.beep(note, 0.2 / arpeggio, vol)

# motor.stop()

hub.speaker.play_sound("sound")
