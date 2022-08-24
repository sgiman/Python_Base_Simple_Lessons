# coding=utf-8
# ******************************************
# 006 - Циклы For, While, а также операторы
# Gosha Dudar, 2017
# **********************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
#
import end as end

i = 0
while i <= 10:
    print(i)
    i += 2

print("")

i = 1000
while i > 100:
    print(i)
    i /= 2

for j in 'hello world':
    if j == 'w':
        break               # continue
    print(j * 2, end='')  # с выводом в одну строку

for j in 'hello world':
    if j == 'a':
        break               # continue
    # print(j * 3, end = '')  # с выводом в одну строку
else:
    print ("\nБуквы а нету в слове")
