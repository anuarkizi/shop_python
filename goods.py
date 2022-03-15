# Товар
class Goods(object):
    global shopy
    def __init__(self,id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

        # При печати объектов выводится содержимое

    def goods(self):
        self.shopy = []
        self.shopy.append(self.id)
        self.shopy.append(self.name)
        self.shopy.append(self.price)
        self.shopy.append(self.stock)
        return self.shopy


# if __name__ == '__main__':
#     goods = Goods('Apple pods', 2999, 100)
#     print(goods)
#     goods2 = Goods('Apple Watch', 3666, 100)
