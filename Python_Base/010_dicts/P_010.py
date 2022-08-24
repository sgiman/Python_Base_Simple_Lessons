# coding=utf-8
# ****************************************
# 010 - Словари (dict), а также их методы
# Gosha Dudar, 2017
# ****************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# ----------------------------------------
# key : value
#

# -1-
print("\n*** LIST DICTIONARY ***")
d = {'test': 1, 'test_2': "TeST"}
print(d)
print(d['test'])
print(d['test_2'])

# -2-
print("\n*** DICTIONARY ***")
d = dict(short='dict', longer='dictionary')
print(d)
d['short'] = 234
print(d)

# -3-
# Словарь в виде списка с кортеджами - (key, value)
d = dict([(23, 24), (56, 87)])
print(d)

# -4-
# Словарь из ключей
d = dict.fromkeys(['a', 'b', 'c'], 1) # заполнить все ключи velue = 1
print (d)

# -5-
# заполнение словаря циклом итераций
d = {a: a ** 2 for a in range(7)}   # 7 цеклов для стпени 2
print(d)

# СЛОВАРЬ = {словарь{ФИО} - список[АДРЕС] - словарь{ТЕЛЕФОНЫ}}
print("\n*** PERSON ***")
person = {
    'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},
    'adress': ['r.Андрюшки', 'ул.Васильковская д. 236', 'кв.12'],
    'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23=65', 'mobile_phone_2': 'Нет'}
}
print(person)
print(person['name']['first_name'])
print(person['name']['last_name'])
print(person['adress'][0])
print(person['adress'][1])
print(person['phone']['mobile_phone'])

print(person.values())    # Вывести все значения из словаря
print(person.keys())      # Вывести все ключи из словаря

person.clear()              # Очиотить словарь
print(person)
