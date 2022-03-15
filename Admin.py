from goods import Goods
import xlwt
import xlrd
import  pandas
class Admin:

    "" "Хранить" ""

    def __init__(self):
        pass
    def log(self):
        global t
        t=False
        name=input('login')
        pas=input('password')
        if (name=='admin' and pas=='123' ):
            t=True
            pass
        else:
            print('eror')



    def load(self):
        self.log()
        if t:
            print('Вы хотите добавить товар в базу?: нажмите 1 если да')
            x = input()
            if x=='1':

                "" "Загрузить товар" ""
                sh = []
                sh1 = []
                #

                sh = (pandas.read_excel('man.xls', sheet_name='Sheet1'))
                workbook = xlrd.open_workbook('man.xls')
                #len(sh) - количество строк
                c = 0
                sheet = workbook.sheet_by_index(0)
                while c <= len(sh):
                    sh1.append([sheet.cell_value(c, col) for col in range(0, 4)])
                    c = c + 1
                workbook.release_resources()


                s = int(input('сколько всего наименований?'))
                id_tovara = len(sh)

                book = xlwt.Workbook('man.xls')
                sheet = book.add_sheet('Sheet1')
                cols = ["A", "B", "C", "D"]
                for i in range(s):
                    id_tovara = id_tovara + 1
                    tovary = input('введите название товара')
                    cena = int(input('Цена за 1 кол'))
                    colichestvo = int(input('количество этого товара на складе'))
                    sh1.append(Goods(id_tovara, tovary, cena, colichestvo).goods());

                for i in range(len(sh1)):
                    row = sheet.row(i+1)
                    for index, col in enumerate(cols):
                        value = sh1[i][index]
                        row.write(index, value)
                book.save("man.xls")




