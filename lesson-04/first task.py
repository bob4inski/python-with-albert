class Reader:
    __books = []
    def __init__(self,name):
        self.name = name

    def takeBook(self,book):
        if len(self.__books) < 2:
            self.__books.append(book)
            print(f'{self.name} взял {book}' )
        else:
            print(f'{self.name} не может взять книгу' )

    def returnBook(self,book):
        if len(self.__books) == 0:
            print(f'{self.name} уже сдал все книги')
        else:
            self.__books.remove(book)
            print(f'{self.name} сдал {book}')

robert = Reader('Robert')
robert.takeBook('fffff')
robert.takeBook('fffff')
robert.takeBook('fffff')
robert.returnBook('fffff')






'''class Books:
    def __init__(self,listOfBooks):'''


