class Worker:
    wage_bonus = {"first_class": {"wage": 100, "bonus": 20}, "second_class": {"wage": 150, "bonus": 21},
                  "third_class": {"wage": 200, "bonus": 50}}

    name = ""
    surname = ""
    position = ""
    __income = ""

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = self.wage_bonus[income]

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return Worker.get_total_income(self)


pos = Position("John", "Do", "Manager", "first_class")
print(pos.get_full_name())
print(pos.get_total_income())