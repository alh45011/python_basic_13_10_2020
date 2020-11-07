class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number < other.number:
            raise ArithmeticError("Subtraction is not possible. Left.number is less than Right.number")

        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        if other.number == 0:
            raise ArithmeticError("Division is not possible. Left.number is equal to 0")

        return Cell(int(self.number / other.number))

    def make_order(cls, cell_number):
        row_number = cls.number // cell_number
        result = ""
        for _ in range(row_number):
            result += cell_number * "*" + "\n"

        if cls.number % cell_number != 0:
            result += cls.number % cell_number * "*"

        return result

cell1 = Cell(52)
cell2 = Cell(10)

cell3 = cell1 - cell2
print(cell3.number)

print(Cell.make_order(cell1, 10))

#print(5 * "str")
