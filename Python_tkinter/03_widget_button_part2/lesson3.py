# ************************************
# 003 - Виджет Button. Часть 2
# ************************************
# Andrey Kudlay (WebForMySelf), 2019
# ------------------------------------
# Writing by sgiman @ 2022, aug
#

from tkinter import *
import time

# --- Окно ---
win = Tk()
win.title('Counter')                    # title
win.iconbitmap('../res/D-ICON.ico')     # icon
win.geometry('600x400+600+300')         # size & position
win.resizable(False, False)             # enable resize (width, height)
win['bg'] = 'blue'                      # background


def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')    # получить текущее время (часы:минуты:секунды)
    # print(time.strftime('%H:%M:%S'))


clicks = 0          # кол-во кликов


def counter():
    global clicks   # глобальная пременная для кол-во кликов
    clicks += 1
    win.title(f'Counter: {clicks}')


btn_time = Button(win, text="Check time", command=check_time)   # кнопка с текущим временем
btn_time.pack()                                                 # отобразить

btn_cnt = Button(win, text="Counter", command=counter)          # кнопка для кол-ва кликов
btn_cnt.pack()                                                  # отобразить

win.mainloop()     # главный цикл событий окна win
