class Washing:
    def __init__(self, water):
        self.water = water

    def do(self, item):
        self.item = item
        print(f'я стираю {item} с кучей ( а точнее {self.water}) литров  воды ептыыыыть')


class Driving:
    def do(self,a, b):
        print(f'я везу из {a} в {b}')


class Mashine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color


class Washing_mashine(Mashine, Washing):
    def __init__(self, brand, price, year, color, water):
        Mashine.__init__(self, brand, price, year, color)
        Washing.__init__(self, water)
        


class Driving_Mashine(Mashine, Driving):
    pass


stiralka = Washing_mashine('canon', 100000, 1999, 'red', 13)
stiralka.do('вещи')

dodge = Driving_Mashine('dodge', 100000, 1976, 'blask')
dodge.do('Казахстан', 'Грозный')

    