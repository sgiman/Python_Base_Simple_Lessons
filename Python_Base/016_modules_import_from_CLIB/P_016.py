# coding=utf-8
# *************************************
# 016 - Модули. Работа с import и from
# Gosha Dudar, 2017
# *************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# -------------------------------------
# python, C, C++
#

# import math, time, os

import math
import os
import random as r  # Сокращения через псевдоним
import time

print("\n*** math ***")
print("math.e = \n\t", math.e)
print("math.pi = \n\t", math.pi)
print("math.cos(1) = \n\t", math.cos(1))

print("\n*** time, os ***")
print(time.time())  # Кол-во сек. с 01.01.1970
print(os.getcwd())  # Путь к файлу
# print(os.uname())             # SysInfo
print(r.random())  # Случайное число от 0 до 1

try:
    import nomodule
except ImportError:
    print("Модуль nonmodule не сущетвует")

# print ("\n*** НОВЫЙ МОДУЛЬ ***")
# import module as m
# m.hi ()
# print (m.add (45, 15))

from module import hi as h, add as a  # Импортировать из модуля только фукцию hi (поседоним h)

h()  # Можно пролучить имя или псевдоним модуля (псевдоним a)
print(a(45, 15))
