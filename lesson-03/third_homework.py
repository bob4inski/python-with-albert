import random
class Cars:
    def __init__(car, speed, name):
        car.status = 'Still alive'  # can be broken or still alive
        car.speed = speed  # car speed
        car.name = name

    def __lt__(self, other):
        return self.speed < other.speed

def get_speed(car):
    return car.speed



class Race:
    lenght_of_lap = 5  # km

    def __init__(rase, list_of_cars: list, laps: int):
        rase.list_of_cars = list_of_cars
        rase.laps = laps


    def play(rase):

        result = sorted(rase.list_of_cars,reverse = True)
        for i in range(rase.laps):
            lenght = len(rase.list_of_cars) - 1
            #rase.list_of_cars = sorted(rase.list_of_cars, key = get_speed,reverse=True)
            trash_1 = random.randint(0,lenght-1)
            x = result.pop(trash_1)
            result.append(x)
        return result

def spisok_cars(N):
    result = []
    names = ['BMW','Dodge','Lotus','Lada','Ferrari','Volvo','Mersedes','Toyota','Wolks']
    for i in range(N):
        carrr = Cars(random.randint(150,300),random.choice(names))
        result.append(carrr)
        carrr = None
    return result

def sort_by_speed(a):
    swapped = False
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[i].get_speed() > a[j + 1].get_speed():
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return a

def outt(a):
    ar = []
    for i in a:
        ar.append(f'{i.name} {i.speed}')
    print(ar)


listcar = spisok_cars(10)
outt(listcar)

N = 5
rase_try = Race(listcar, N)
outt(rase_try.play())

