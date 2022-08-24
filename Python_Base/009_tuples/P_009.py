# coding=utf-8
# ******************************************
# 009 - Кортежи (tuple)
# ******************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# ------------------------------------------
# важные спмски, которые нельзя изменять
# кортдежи по размеру памяти меньше списков
#
a = (43, 56, 45.23, 'd')    # КОРТЕДЖ
b = [43, 56, 45.23, 'd']    # СПИСОК

# a[0] = 34 # ошибка
b[0] = 34

print (a.__sizeof__())
print (b.__sizeof__())

a = tuple("hello world")        # разделить на символы
print(a)

a = "hello world"               # строка
print(a)

a = ("hello world", "sdf", 345) # кортедж
print(a)
print (a.count(345))            # определить чиоло элементов "345"
