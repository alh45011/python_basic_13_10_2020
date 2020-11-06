class Road:
    __length = ""
    __width = ""

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_mass_asphalt(self, material_thickness, mass_1_m):
        return (self.__length * self.__width * material_thickness * mass_1_m) / 1000


road = Road(20, 5000)
print(road.calc_mass_asphalt(25, 5))