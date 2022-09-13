# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    fibArray = [0]
    if n > 0:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
            fibArray.append(a)
        a, b = 0, 1
        for i in range(n):
            a, b = b, a - b
            fibArray.insert(0, a)
    return fibArray


n = int(input("Введите число: "))
print(Fibonacci(n))
