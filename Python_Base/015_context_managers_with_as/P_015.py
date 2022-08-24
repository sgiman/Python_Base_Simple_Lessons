# coding=utf-8
# **************************************
# 015 - Менеджеры контекста With ... as
# Gosha Dudar, 2017
# **************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug

# Защита от ошибок ввода не числа (123...). При ошибке ввода файл закрывается

with open('text.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input('Number: '))
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write (line)
