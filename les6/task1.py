import datetime as dt

class TrafficLight:
    __color = ""

    _modes = []
    _modes_time = {}
    __current_mode = 0

    def __init__(self):
        self._modes = ["red", "yellow", "green"]
        self._modes_time = {"red": 7, "yellow": 2, "green": 5}

    def running(self):
        current_time = dt.datetime.now()
        modes = self._modes
        current_time_diff = self._modes_time[modes[self.__current_mode]]
        while True:
            if (dt.datetime.now() - current_time).total_seconds() > current_time_diff:
                current_time = dt.datetime.now()
                print("Now is ", modes[self.__current_mode])
                self.__current_mode = (self.__current_mode + 1) % len(modes)
                current_time_diff = self._modes_time[modes[self.__current_mode]]


tl = TrafficLight()
tl.running()

