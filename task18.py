'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random


array = []
sick = 0
shift = 1
flag = False

for i in range(int(input('Введите размер массива: '))) :
    sick += 1
    array.append(random.randint(1,sick))
print(array)

x = int(input("Введите X: "))

while(not flag) :
    if x - shift in array and x + shift in array:
        print(f"Наиболее близкий по величине элемент к X = {x - shift} и {x + shift}")
        flag = True
    elif x + shift in array :
        print(f"Наиболее близкий по величине элемент к X = {x + shift}")
        flag = True
    elif x - shift in array :
        print(f"Наиболее близкий по величине элемент к X = {x - shift}")
        flag = True
    else :
        shift += 1




