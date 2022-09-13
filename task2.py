# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

arr = [int(i) for i in input('Введите числа через пробел: ').split()]
for i in range(math.ceil(len(arr) / 2)):
    mult = arr[i] * arr[len(arr) - 1 - i]
    print(mult, end=' ')