import json  # необходимая для работы библиотека

with open('values.json', 'rt', encoding='utf-8') as file1:  # открытие файла со значениями на чтение
    data = file1.read()  # чтение файла
    values = json.loads(data)['values']  # сразу проваливаемся в словарь values

with open('tests.json', 'rt', encoding='utf-8') as file2:
    data = file2.read()
    tests = json.loads(data)


def look_for_value(element):  # функция для рекурсии
    for i in range(len(element)):  # чтобы прошли по всем позициям без пропусков
        if element[i]['id'] == point['id']:  # условие для изменения значения параметра value
            element[i]['value'] = point['value']
        if 'values' in element[i].keys():  # условие для погружения во вложенность
            look_for_value(element[i]['values'])


for point in values:  # прохождение по всем id из файла values
    look_for_value(tests['tests'])

text = json.dumps(tests)  # упаковываем JSON словарь с втроку для последующей записи

with open('report.json', 'wt', encoding='utf-8') as file3:  # открытие файла на запись
    file3.write(text)  # запись в файл
