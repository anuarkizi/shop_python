

from Admin import Admin
from Shop import Shop
import xlwt
import xlrd
import  pandas


person=input('Нажмите 1 - если вы Admin, 2 - если вы покупатель')


if person=='1':
    admin = Admin()
    print('login: admin password: 123 ')
    admin.load()

if person=='2':
    shops=[]
    workbook = xlrd.open_workbook('man.xls',formatting_info=True)
    sheet = workbook.sheet_by_index(0)
    len=0
    for i, row in sheet.rowinfo_map.items():
        len+=1

    c = 0
    sheet = workbook.sheet_by_index(0)
    while c < len:
        shops.append([sheet.cell_value(c, col) for col in range(0, 4)])
        c = c + 1

    shop = Shop(shops)
    shop.run()

