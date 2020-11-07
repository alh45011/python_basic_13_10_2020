from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def consumption(self) -> float:
        pass

    @property
    @abstractmethod
    def params(self) -> float:
        pass


class Suit(Wear):

    def __init__(self, name: str, height: float):
        self.__height = height
        self.name = name

    @property
    def consumption(self) -> float:
        return 2 * self.__height + 0.3

    @property
    def params(self) -> float:
        return self.__height


class Coat(Wear):
    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def consumption(self) -> float:
        return self.__size / 6.5 + 0.5

    @property
    def params(self) -> float:
        return self.__size


coat = Coat("Броское", 25)
print(coat.consumption)
#coat.consumption = 22