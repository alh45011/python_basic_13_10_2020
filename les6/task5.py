class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Pen"

    def draw(self):
        print("Рисование ручкой")


class Pencil(Stationery):
    title = "Pencil"

    def draw(self):
        print("Рисование Карандашём")


class Handle(Stationery):
    title = "Handle"

    def draw(self):
        print("Рисование Маркером")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()