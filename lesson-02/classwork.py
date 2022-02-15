'''class Bakery:
    def __init__(self,eggs,flour):
        self.eggs = eggs
        self.flour = flour
    def bake(self, temp, time):
        
class Cookie(Bakery):
    def __init__(cinnamon):
        super().__init__(eggs, flour)
        self.cinnamon = cinnamon
    def __del__(self):

b = Bakery()
b.bake(180,900)'''

class Car:
    steering_wheel = True
    def __init__(self,color,engine,wheels):
        self.color = color
        self.engine = engine
        self.wheels = wheels
    
    def drive(self, speed,a,b,list_of_load):
        time = (b - a) / speed
        for item in list_of_load:
            item.place = b

class Ferrari(Car):
    def __init__(self, color, engine, wheels):
        if not(engine == 'V8' or engine == 'V12'):
            print('Error')
            raise Exception
            return
        else:
            super().__init__(color,engine,wheels)
            self.manufactory = 'Ferrari'
            

car_2 = Ferrari('red','V8',4)
print(car_2.manufactory)

dodge = Car('black','W8',6)
print(dodge.color)