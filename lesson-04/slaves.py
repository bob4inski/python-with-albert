import typing
class Engine:
    def __init__(self,weight,q,power,volume):
        self.weight = weight
        self.power = power
        self.volume = volume
        self.q = q

class Wheel:
    def __init__(s,weight,q,mft,radius):
        s.weight = weight
        s.mft = mft
        s.radius = radius
        s.q = q

class Steering:
    def __init__(s,weight,q,mft,shape):
        s.weight = weight
        s.mft = mft
        s.q = q
        s.shape = shape

        if s.mft == 'eng' or s.mft == 'jpn':
            s.place = 'right'
        else:
            s.place = 'left'

class Car:
    def __init__(self,eng:Engine,wh:list[Wheel],st:Steering):
        weight_of_all = sum([item.weight for item in [eng,st]])
        self.hp =eng.power / weight_of_all
        self.engine  = eng
        self.wheels = wh
        self.steeringWheel = st
        q_wh = sum([w.q for w in wh]) / len(wh)
        self.q = (eng.q + q_wh + st.q ) / 3
        self.place = st.place

Eng = Engine(200,10,145,3)
Whls = Wheel(10,10,'rus',17)
ster = Steering(2,10,'jpn','square')
Nissan = Car(Eng,[Whls,Whls,Whls,Whls],ster)
print(Nissan.place)

