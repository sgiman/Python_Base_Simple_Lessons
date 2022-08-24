# coding=utf-8
# ********************************************
# 013 - Исключения (Конструкция try - except)
# Gosha Dudar, 2017
# ********************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# --------------------------------------------
# print (10/0)
# print (int ('qwert'))
# print ('2' + 1)

print("\n*** X / Y (1) ***")
x = int(input('X = '))
y = int(input('Y = '))
try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели 0")
    res = 0
print(res)

print("\n*** 2 ***")
try:
    x = int(input())
except ValueError:
    print("Вы ввели не число")
    x = 0
print(x)

print("\n*** X / Y (all try-except) ***")
try:
    x = int(input('X = '))
except ValueError:
    print("Вы ввели не число")
    x = 0
else:
    print("Все верно - X")
finally:
    print("Введен X")

try:
    x = int(input('Y = '))
except ValueError:
    print("Вы ввели не число")
    y = 0
else:
    print("Все верно - Y")
finally:
    print("Введен Y")

try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели 0")
    res = 0
else:
    print("Все верно - X/Y")
finally:
    print("Результат Y")

print(res)
