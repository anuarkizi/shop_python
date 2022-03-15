from goods import Goods


class CartItem(object):
    # Корзина товаров
    def __init__(self, goods, count):
        self.goods = goods
        self.count = count

    def __str__(self):
        # % f является заполнителем для десятичного типа
        return '%s(￥%.2f)*%s' % (self.goods[1],
                                 self.goods[2], self.count)

        # Рассчитать подытог продукта

    def amout(self):
        return self.goods[2] * self.count


