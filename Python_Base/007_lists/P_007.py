# coding=utf-8
# ********************
# 007 - Списки (list)
# Gosha Dudar, 2017
# **********************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
#

l = []  # пустой список
lis = [1, 56, 'x', 34, 1.34, ['S', 't', 'r', 'o', 'k', 'a']]
print(lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(23)        # добавляет элемент
l.append(34)
b = [24, 67]
l.extend(b)         # расширяет другим списком
l.insert(1, 60)     # вставляет по индексу
l.append(34)
l.remove(34)        # удаляет первый элемент при совпадении
l.pop()             # удаляет последний или i-тый элемент
print(l.index(24))  # определить индекс
print(l.count(34))  # возвращает номер индекса
l.sort()            # сортировка
l.reverse()         # ревертирование
l.clear()           # очистить список

print(l)
