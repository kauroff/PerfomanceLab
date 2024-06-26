circle = input()  # пути к файлам передаются программе в качестве аргументов
points = input()

with open(circle, 'rt', encoding='utf-8') as file1:  # открытие файла с окружностью в режиме чтения
    data = file1.read()  # чтение файла
    crdnts, radius = data.split('\n')  # разбиение на данные
    x = int(crdnts[0])
    y = int(crdnts[2])
    r = int(radius)

with open(points, 'rt', encoding='utf-8') as file2:
    data = file2.read()
    points = data.split('\n')

for point in points:  # проходимся по каждой точке из файла2
    x1 = int(point[0])
    y1 = int(point[2])
    if (x - x1) * (x - x1) + (y - y1) * (y - y1) == r * r:  # условие нахождение в круге
        print(0)
    elif (x - x1) * (x - x1) + (y - y1) * (y - y1) < r * r:  # условие нахождение на окружности
        print(1)
    else:  # иначе вне круга
        print(2)

