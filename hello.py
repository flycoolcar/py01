print('hello')
print('hello')
print('hello')
print(1111111111111)

class book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def say_price(self):
        print(f'书的价格是:{self.price}')


class book_my(book):
    def __init__(self,name,price,color):
        book.__init__(self,name,price)
        self.color = color
        


b1= book('abc',20)
print(b1.name,b1.price)
b1.say_price()