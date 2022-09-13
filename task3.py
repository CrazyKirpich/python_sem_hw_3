# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# arr = [float(i) for i in input('Введите числа через пробел:\n').split()]
# maxFloat = minFloat = 0
# for i in arr:
#     if i % 1 != 0 and maxFloat < round(i % 1, 2):
#         maxFloat = round(i % 1, 2)
#     elif i % 1 != 0 and minFloat > round(i % 1, 2):
#         minFloat = round(i % 1, 2)
# print(maxFloat - minFloat)

# Вопрос, где в решении сверху ошибка?
# Почему округляет [1.1, 1.2, 3.1, 5, 10.01] до 0.2?
# Хотя все тоже самое в компактном решении ниже, 
# но ответ выдает правильный - 0.19

arr = [float(i) for i in input('Введите числа через пробел: ').split()]
print(max(round(i % 1, 2) for i in arr if i % 1 != 0) -
      min(round(i % 1, 2) for i in arr if i % 1 != 0))
