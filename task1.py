# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# arr = [int(i) for i in input('Введите числа через пробел: ').split()]
# sum = 0
# for i in range(1, len(arr), 2):
#     sum += arr[i]
# print(sum)

arr = [int(i) for i in input('Введите числа через пробел: ').split()]
print(sum(arr[1::2]))
