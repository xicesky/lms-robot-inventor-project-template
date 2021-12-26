from typing import Any, Callable


class Timer:
    def __init__(self) -> None:
        """
        Timers track time for events

        Attributes
        ----------
        ...  # can we observe the internal state?

        Examples
        --------

        ```python
        from mindstorms.control import Timer, wait_for_seconds

        print("creating Timer...")
        timer = Timer()
        wait_for_seconds(5)
        print("seconds elapsed:", timer.now())
        ```
        """
        ...

    def reset(self) -> None:
        """reset Timer state to 0

        The internal timer state counts from when the Timer object is
        initialized. The ``reset()`` method can be used to clear that
        state to count from a new temporal position.
        """
        ...

    def now(self) -> int:
        """retrieve the "right now" of the Timer

        The Timer state is the number of seconds since the Timer was
        initialized or last reset. Since this return value is an
        integer, the resultion of this method is 1 sec and cannot be
        used for precise timing functionality.

        When comparing, it is advisable to use an "or equal to"
        comparison to avoid the code execution from passing the desired
        target time without performing the desired action (e.g. stopping
        a motor).

        Returns
        -------
        now : int
            number of seconds since Timer initialized/reset
        """
        ...


def wait_for_seconds(seconds: int) -> None:
    """wait for a specified number of seconds before continuing

    Blocking routine that pauses execution of the program for the
    specified number of seconds.

    Parameters
    ----------
    seconds : int
        time to wait, in seconds

    Raises
    ------
    TypeError
        ``seconds`` is not a number
    ValueError
        ``seconds`` is not at least 0
    """
    ...


def wait_until(
    get_function_value: Callable, operator_function: Callable, target_value: Any = True
) -> None:
    """wait until the condition is met before continuing

    Blocking routine that waits until the condition defined by the
    ``operator_function`` is met when comparing the value returned by
    ``get_function_value`` to the ``target_value``. The
    ``get_function_value`` parameter should be one of the methods that
    actively request the device value, and the ``operator_function``
    parameter should be one of those defined in ``mindstorms.operator``.

    Examples
    --------
    The below can be copy-pasted into a new Python project in the
    Mindstorms app and run on-device.

    ```python
    from mindstorms import ColorSensor
    from mindstorms.control import wait_until
    from mindstorms.operator import equal_to

    color_sensor = ColorSensor("A")

    # Wait for the Color Sensor to detect "red."
    wait_until(color_sensor.get_color, equal_to, "red")
    ```

    Parameters
    ----------
    get_value_function : f
        function that returns a current value
    operator_function: f
        function comparing two arguments
    target_value: Any, default True
        value output is checked against
    """
    ...
