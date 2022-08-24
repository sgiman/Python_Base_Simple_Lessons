# ************************************
# 002 - Виджет Button. Часть 1
# ************************************
# Andrey Kudlay (WebForMySelf), 2019
# ------------------------------------
# Writing by sgiman @ 2022, aug
#


from tkinter import *

# ---- window ----
win = Tk()
win.title('First GUI')                  # title
win.iconbitmap('../res/D-ICON.ico')     # icon
win.geometry('600x400+600+300')         # size & position
win.resizable(False, False)             # enable resize (width, height)
win['bg'] = 'blue'                      # background


# ------------------------------
# clicked() - фукция для кнопки
# ------------------------------
def clicked():
    print('Clicked')


# btn = Button(win, text="Кнопка", command=clicked, font="Arial 20 italic")
# btn = Button(win, text="Кнопка", command=clicked, font=("Comic Sans MS", 20))
btn = Button(win, text="Кнопка 1\n22", justify=CENTER)  # текст кнопки c выравниванием текста
btn.configure(width=20)                                 # ширина кнопки
# btn['font'] = 'Arial 15'
btn.pack()                                              # отобразить кнопку

win.mainloop()  # главный цикл событий окна
