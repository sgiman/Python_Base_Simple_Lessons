# coding=utf-8
# *******************************
# 017 - Основы ООП Python
# Gosha Dudar, 2017
# *******************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
#

# *************
#     Класс
# *************
class Person:
    name = "Ivan"  # Параметры
    age = 10

    def set(self, name, age):  # Метод, self - содержит экземпяор класса (this)
        self.name = name
        self.age = age


# vlad = Person()               # Объект класса Person
# vlad.name = "Влад"
# print(vlad.name)
# ivan = Person()               # Новый объект класса Person
# ivan.age = 45
# print(ivan.name)
# print(ivan.age)

print("\n*** 1 ***")
vlad = Person()  # Новый объект класса Person
vlad.set("Влад", 25)  # Новые характеристики объекта для класса
print(vlad.name + " " + str(vlad.age))

print("\n*** 2 ***")
ivan = Person()  # Новый объект класса Person
ivan.set("Иван", 56)  # Новые характеристики объекта для класса
print(ivan.name + " " + str(ivan.age))
