n, m = input().split()  # вводные данные
array = []  # исходный массив
answer = []  # ответ, пока пустой список
kit = [0]  # интервал, пока из 1 элемента
k = 0  # счетчик
q = int(m)  # счетчик
if int(n) == 0 or int(m) == 0:  # проверка на корректность входных данных
    print()
else:
    for l in range(int(m)):
        for i in range(int(n)):  # в матрице m*n гарантировано будет хотя бы 1 подходящий нам элемент
            array.append(i + 1)  # исходный массив начинается с 1
    while True:
        kit = array[k:q]  # проходимся по всем интервалам, изначально от 0 до m
        answer.append(kit[0])  # добавляем к ответу первый символ из интервала
        k += int(m) - 1  # меняем счетчик
        q += int(m) - 1  # меняем счетчик
        if kit[-1] == 1:  # проверка условия - последний знак равен -1
            break  # в этом случае останавливаем программу

    print(str(answer).strip('[]').replace(', ', ''))  # вывод ответа в консоль в нужном формате
