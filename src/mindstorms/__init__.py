# estimated code from compiled .mpy files

from _api.speaker import *
from _api.large_technic_hub import *

MSHub = LargeTechnicHub  # _api.large_technic_hub.LargeTechnicHub


# better user-friendliness code?
class MSHub:
    """
    the Mindstorms brain

    The MSHub ("Hub") is the embedded system that runs all Mindstorms
    programs and allows up to six peripherals (motors, sensors, etc.) to
    be connected and controlled. The Hub can be connected to through a
    wired USB connection or via Bluetooth.

    Attributes
    ----------
    left_button : Button
    right_button : Button
    """

    speaker : Speaker


    def __init__(self) -> None:
        ...


class Motor:
    def __init__(self, port) -> None:
        ...

    def run_to_position(self, degrees, direction='shortest_path', speed=None) -> None:
        ...
    def run_to_degrees_counted(self, degrees, speed=None) -> None:
        ...
    def start(self, speed=None) :
        ...
    def start_at_power(self, power) :
        ...
    def stop(self) -> None :
        ...
    def run_for_degrees(self, degrees, speed=None) :
        ...
    def run_for_rotations(self, rotations, speed=None) :
        ...
    def run_for_seconds(self, seconds, speed=None) :
        ...

    def get_position(self) -> int : ...
    def get_speed(self) -> int: ...
    def get_degrees_counted(self) -> int: ...
    def get_default_speed(self) -> int: ...

    def was_interrupted(self) -> bool: ...
    def was_stalled(self) -> bool: ...

    def set_degrees_counted(self, degrees_counted) -> None : ...
    def set_default_speed(self, default_speed) -> None : ...
    def set_stop_action(self, action='coast') -> None : ...
    def set_stall_detection(self, stop_when_stalled=True) -> None: ...

class MotorPair:
    def __init__(self) -> None:
        ...


class ColorSensor:
    def __init__(self) -> None:
        ...


class DistanceSensor:
    def __init__(self) -> None:
        ...


class App:
    def __init__(self) -> None:
        ...
