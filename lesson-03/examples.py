class ExQuote:
    def __init__(self,quote):
        self.quote = quote

    def say(self):
        return self.quote + '!'

class QQuote:
    def __init__(self,quote):
        self.quote = quote

    def say(self):
        return self.quote + '?'

a = QQuote('ты кто нахуй')
b = ExQuote('Изикей')
print(a.say())
print(b.say())



