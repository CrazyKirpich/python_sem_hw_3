# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input("Введите число : "))
# s = ''
# while n >= 2:
#     s = str(n % 2) + s
#     n = n // 2
# s = str(n) + s
# print(s)

print(bin(int(input('Введите число: ')))[2::])
