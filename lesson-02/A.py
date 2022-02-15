class A:
    def shout(self):
        print('what is your name')
    def say(self):
        print('I am obj A')

class B:
    def yell(self):
        print('Exekiel')
    def say(self):
        print('I am obj B')

class C(B,A):
    pass

arddr = C
arddr.say(arddr)