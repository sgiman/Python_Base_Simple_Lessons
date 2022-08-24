# coding=utf-8
# *********************************************
# 019 - Конструкторы, переопределение методов
# Gosha Dudar, 2017
# *********************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
#

# ***********
#    Класс
# ***********
class Person:
    name = "Ivan"  # Параметры
    age = 10

    def __init__(self, name, age):  # Конструктор и инициализация
        self.name = name
        self.age = age

    def set(self, name, age):  # Метод, self - содержит экземпяор класса (this)
        self.name = name
        self.age = age


class Student(Person):  # Наследование основного класса Person
    course = 1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


igor = Student("Вася", 19)
igor.set("Игорь", 23, 5)
print("\nИмя:", igor.name, ", возраст -", igor.age, ", курс -", igor.course)

print("\n*** 1 ***")
vlad = Person("Влад", 25)  # Новый объект класса Person
print(vlad.name + " " + str(vlad.age))

print("\n*** 2 ***")
ivan = Person("Иван", 56)  # Новый объект класса Person
print(ivan.name + " " + str(ivan.age))
