
menu = '___МЕНЮ___\n1)ввести данные\n2)вывести все введенные данные\n3)выход'
storage = {}
while True:
    print(menu)
    a = input()
    if a == '1':
        print('Введите название товара')
        name = input()
        print('Введите колличество товара')
        qty = input()
        print('Введите стоимость товара')
        price = input()
        storage[name] = [f'колличество:{qty}', f'стоимость:{price}']
    if a == '2':
        print('СПИСОК ТОВАРОВ')
        for key in storage:
            print(key, '->', storage[key])

    if a == '3':
        print('До скорой встречи!')
        break