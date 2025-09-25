class HourError(Exception):
    def __init__(self, value):
        self.value = value
class MinuteError(Exception):
    def __init__(self, value):
        self.value = value
class SecondError(Exception):
    def __init__(self, value):
        self.value = value

class Clock:
    def __init__(self, hr: int, min: int, sec: int):
        i = 0
        if type(i) != type(hr):
            raise TypeError("Hour must be an integer")
        if type(i) != type(min):
            raise TypeError("Minute must be an integer")
        if type(i) != type(sec):
            raise TypeError("Second must be an integer")
        if hr < 0 or hr > 23:
            raise HourError(f"{hr} is not a valid hour")
        if min < 0 or min > 59:
            raise MinuteError(f"{min} is not a valid minute")
        if sec < 0 or sec > 59:
            raise SecondError(f"{sec} is not a valid second")
        self.hour = hr
        self.minute = min
        self.second = sec
    def __add__(self, right):
        h = 0
        m = 0
        s = (self.second + right.second)
        if s > 59:
            s = s % 60
            m = m + 1
        m = (self.minute + right.minute + m)
        if m > 59:
            m = m % 60
            h = h + 1
            
        h = (self.hour + right.hour + h) % 24
        return Clock(h, m, s)

   