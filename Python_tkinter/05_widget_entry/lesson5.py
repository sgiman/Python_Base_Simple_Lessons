# **************************************
# 005 - Виджет Entry
# **************************************
# Andrey Kudlay (WebForMySelf), 2019
# ------------------------------------
# Writing by sgiman @ 2022, aug
#

from tkinter import *

# ---- window ----
win = Tk()
win.title('Input')                      # title
win.iconbitmap('../res/D-ICON.ico')     # icon
win.geometry('400x240+600+300')         # size & position
win.resizable(True, True)               # enable resize (width, height)
win['bg'] = 'blue'                      # background


# Add "HELLO"
def add_str():
    e.insert(END, 'HELLO WORLD !!!')


# Delete Text
def del_str():
    e.delete(0, END)


# Get Text
def get_str():
    lout_text['text'] = e.get()


# Label for Entry Widgets
l = Label(win, text="Поле ввода:", bg="blue", fg='white')
l.pack()

# Entry widgets (ввод-вывод данных)
e = Entry(win, width = 30)
e.insert(0, 'Hello')
e.insert(END, ' world !')
e.place(x = 140, y = 20)

# --- BUTTONS ---
btn_add = Button(win, text="Add", command=add_str)      # button "Add"
btn_del = Button(win, text="Delete", command=del_str)   # button "Delete"
btn_get = Button(win, text="Get", command=get_str)      # button "Get"

btn_add.place(x = 10, y = 20)                           # Place and position for button "Add"
btn_del.place(x = 50, y = 20)                           # Place and position for button "Delete"
btn_get.place(x = 100, y = 20)                          # Place and position for button "Get"

lout_text = Label(win, bg='blue', fg='white')          # Label for output field
lout_text.place(x = 140, y = 50)                        # отобразить

win.mainloop()  # главный цикл событий окна win

'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. 
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''
