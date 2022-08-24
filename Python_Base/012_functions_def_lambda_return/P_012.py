# coding=utf-8
# ************************************
# 012 - Функции (def, lambda, return)
# Gosha Dudar, 2017
# ****************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug

print('\n*** 1 ***')


def func(x):
    return x


print(func(23))

print("\n*** 2 ***")


def func(x, a):
    return x + a


print(func(23, 12))

print("\n*** 3 ***")


def func(x, a):
    return x + a


print(func('Hello', ' World!'))

print("\n*** 4 ***")


def func(x, a):
    res = x + a
    return res


print(func('Hello', ' World!'))

print("\n*** 5 ***")


def func(x):
    def add(a):
        return x + a

    return add


test = func(100)  # подготовка: получитть ссылку на функцию test с первым аргументои 100
print(test(250))  # результат после выполнения test
print("\n*** Empty Function ***")


def func():
    pass


print(func())
print("\n*** 5 ***")


def func(r, w, y=2):
    return r + w + y


print(func(2, 4))           # могут быть только 2 аргумента
print(func(2, 4, 5))        # все аргументы

print("\n*** 6 ***")


def func(*args):
    return args


print(func('sd', 4, 34.33))                     # кортедж параметров

print("\n*** 6 ***")


def func(**args):
    return args


print(func(a=23, n=56, o=90))                   # словарь параметров
print(func(short='dict', longer='dictionary'))

print("\n*** lambda ***")                       # анонимные функции
add = lambda x, y: x * y
print(add(2, 5))
print(add('q', 5))
print((lambda x, y: x * y)(2, 6))               # сокращенная запись в одну строку
fun = lambda *args: args                        # кортедж параметров
print(fun(2, 56, 78.56))
