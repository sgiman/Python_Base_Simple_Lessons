# coding=utf-8
# ***********************************
# 004 - Переменные
# Gosha Dudar, 2017
# ***********************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# -----------------------------------
# Examples:
# int, float, str          - типы
# str (21)                 - строка
# str (int("21"))          - строка
# str (float("1.12345"))   - строка
# del res                  - удалить переменную
#
# унарные операции
# res +=5
# res -=5
# res *=5
# res /=5
# res %=5  - отстаток
# res **=5 - степень

# string
print("\n*** STRING ***")
name_1 = input("Enter fist name: ")
name_2 = input("Enter second name: ")
name = name_1 + " " + name_2
print("Result is", name)

# int
print("\n*** INTEGER ***")
num_1 = int(input("Enter fist int: "))
num_2 = int(input("Enter second int: "))
num = num_1 + num_2
print("Result is", num)

# float + int
print("\n*** INT + FLOAT ***")
num_1 = int(input("Enter fist int: "))
num_2 = float(input("Enter second float: "))
res = num_1 + num_2
print("Result is", res)

print("\n*** TEST (RESULT * 5) ***")
Res = input("Enter something text: ")
Res = Res + " "
Res *= 5
print(Res)