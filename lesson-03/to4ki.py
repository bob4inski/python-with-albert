class Dots:
    def __init__(self,x,y):
        self.x = x
        self.y = x

    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x) and (self.y != other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __le__(self, other):
        if self.x == other.x:
            return (self.y > other.y)
        elif self.y == other.y:
            return (self.x > other.x)
        return False

    def __ge__(self, other):
        if self.x == other.x:
            return (self.y < other.y)
        elif self.y == other.y:
            return (self.x < other.x)
        return False

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Dots(x1, y1)

    def __sub__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Dots(x1, y1)

    def __mul__(self, other):
        x1 = self.x * other.x
        y1 = self.y * other.y
        return Dots(x1, y1)
    def get(self):
        print(self.x,self.y)

to4ka_a = Dots(1,2)
to4ka_b = Dots(2,3)
to4ka_c = to4ka_a.__add__(to4ka_b)
to4ka_c.get()


