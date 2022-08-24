# ******************************************************************
# 001 - Что такое Tkinter
# https://www.tutorialspoint.com/python3/python_gui_programming.htm
#
# ******************************************************************
# Andrey Kudlay (WebForMySelf), 2019
# ------------------------------------------------------------------
# Writing by sgiman @ 2022, aug
#
from tkinter import *

# --- Окно ---
window = Tk()                           # подключить бибиотеку Tkinter
window.title('First GUI')               # title
window.iconbitmap('../res/D-ICON.ico')  # icon
window.geometry('600x400+600+300')      # size & position
window.resizable(False, False)          # enable resize (width, height)

# Фон окна 
# window.config(bg='#000')              # вариант 1
window['bg'] = 'blue'                   # вариант 2

window.mainloop()                       # главный цикл событий окна
