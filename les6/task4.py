class Car:
    speed = ""
    color = ""
    name = ""
    is_police = ""

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "go"

    def stop(self):
        return "stop"

    def turn(self, direction):
        return "turned to " + direction

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        Car.show_speed()
        if self.speed > 60:
            print("Speed is too hight!")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        Car.show_speed()
        if self.speed > 40:
            print("Speed is too hight!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)


police_car = PoliceCar(40, "red", "chevrole")
police_car.show_speed()
