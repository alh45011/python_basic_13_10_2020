class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ""
        for row in range(len(self.data)):
            result += str(self.data[row])
            if row != len(self.data) - 1:
                result += "\n"
        return result

    def __add__(self, other):
        result = Matrix([],)
        for row in range(len(self.data)):
            result.data.append([],)
            for el in range(len(self.data[row])):
                result.data[row].append(self.data[row][el] + other.data[row][el])
        return result



matrix = Matrix([[1, 2, 3], [4, 4, 4], [5, 3, 2]])
print(matrix)
matrix2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print("")

matrix3 = matrix + matrix2
print(matrix3)