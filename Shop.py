from Cartimem import CartItem
import  pandas

class Shop:
    "" "Хранить" ""

    def __init__(self,shops):
        # Хранить все товары
        self.shops=shops
        # Магазин товаров в корзине товаров
        self.cart = []

    def print_line(self):

        print('-' * 50)

    def print_double_line(self):
        print('=' * 50)

    def list(self):
        "" "Список всех товаров" ""
        print("Пожалуйста, выберите продукт:")
        sh = []
        self.print_line()
        sh.append(pandas.read_excel('man.xls', sheet_name='Sheet1'))
        print(sh)
        self.print_line()

    def list_cart(self):
            "" "Показать корзину товаров, рассчитать общую стоимость" ""

            self.print_line()
            total = 0.0
            for item in self.cart:
                print('%s     =%s' % (item, item.amout()))
                total += item.amout()
            self.print_line()
            print("Общая сумма: %.2f всего" % (total))

    def add_to_cart(self):
            "" "Добавить товар в корзину" ""

            print('\n')
            g_id = input( 'Пожалуйста, введите идентификатор продукта (введите, e чтобы оформить заказ, 0, чтобы очистить корзину):')

            if g_id == 'e':
                # Счет, пожалуйста
                total = 0.0
                for item in self.cart:
                    total += item.amout()
                self.print_line()
                print("Пожалуйста, заплатите:.% .2f всего" % (total));

                # Пустая корзина
                self.cart.clear()
                print("Успешный платеж!");

            elif (g_id == '0'):
                    self.cart.clear()
                    print("Корзина        была        опустошена!")
            else:
                    # Рассчитать индекс продукта
                    idx = int(g_id)
                    # Вывезти товар
                    goods = self.shops[idx]
                    self.print_line()
                    print('Вы выбрали ')
                    print(goods[1]+' цена товара '+str(goods[2]))

                    count = int(input('Пожалуйста, введите количество покупки:'))
                    # Определить, больше ли количество, чем инвентарь
                    while count > self.shops[idx][3]:
                            count = int(input('Там не так много товаров, пожалуйста, введите заново:'))

                    # Если товар уже есть в корзине, измените количество товаров
                    # Переменная указывает, есть ли этот продукт в корзине
                    is_exsts = False
                    for item in self.cart:
                        if item.goods == goods:
                            # Объясните, что товар находится в корзине
                            is_exsts = True
                            item.count += count
                            # уменьшить запас
                            self.shops[idx][3] -= count

                            # Если это выполнено, значение is_exsts по-прежнему равно False, что указывает на то, что товара нет в корзине
                    if is_exsts == False:
                        # Добавить товар в корзину
                        self.shops[idx][3] -= count
                        self.cart.append(CartItem(goods, count))

                # Показать корзину товаров и рассчитать общую стоимость
            self.list_cart()

    def run(self):
            "" "Запустить приложение" ""
            print("Магазин        электронных        товаров")
            print('\n')
            #print(shops1)
            self.list()

            while True:
                self.add_to_cart()