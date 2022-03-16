import random
class Cars:
    def __init__(self, speed, name):
        self.speed = speed  # car speed
        self.name = name

def get_speed(car): #просто функция , которая будет выдавать нам скорость машины для сортировки по ключу
    return car.speed

class Race:
    def __init__(self, list_of_cars: list, laps: int): # ну тут инит по обычному
        self.list_of_cars = list_of_cars
        self.laps = laps
    
    def play(self): # а вот тут у нас идет сама функция для игры
        result = sorted(self.list_of_cars, key = get_speed,reverse=True) # сортируем данный нам список машин по скорости и разворачиваем его 
       #в поле ключ мы прописали по какому значению у нас все будет сортироваться
        resultoftrash = [] # создали пустой список для того, чтобы записывать туда всех, кто попадет в аварию
        for i in range(self.laps):
            lenght = len(result)  # это понятно
            trash = random.randint(0,lenght-2) # Выбираем рандомную машину из нашего списка машин, которая попадет в мусорку
            x = result.pop(trash) # причем диапазон для выбора постоянно меняется чтобы мы случайно не выбрали ту же машину второй раз
            resultoftrash.append(x) # понятно
            print(f'выбыл {x.name} {x.speed}') # Выводим название и скорость машины которая выбыла
        return result + resultoftrash[::-1] # возвращаем итоговый список машин и добавили к нему список наших аварийных участников
                                            # главное не забыть его развернуть тк кто первый попал в аварию - последний в гонке и наоборот

def list_of_cars(number): # для удобства тут функция, которая создает список машин 
    result = []             # но список можно обьявить вручную ( ниже я его напишу )
    names = ['BMW','Dodge','Lotus','Lada','Ferrari','Volvo','Mersedes','Toyota','Wolks']
    for i in range(number):
        carrr = Cars(random.randint(150,300),names.pop(random.randint(0,len(names)-1)))
        result.append(carrr)
        carrr = None
    return result

def outt(a): #функция которая позволяет нам нормально все выводить, тк наша функция гонки возвращает массив обьектов
    ar = []
    for i in a:
        ar.append(f'{i.name} {i.speed}')
    print(ar)


listcar = list_of_cars(9)
#или же
#listcar =  ['Ferrari 289', 'Lotus 210', 'BMW 191', 'Wolks 168', 'Toyota 176', 'Dodge 189', 'Mersedes 262', 'Volvo 221', 'Lada 269']

outt(listcar)
N = 5
rase_try = Race(listcar, N) 
outt(rase_try.play())