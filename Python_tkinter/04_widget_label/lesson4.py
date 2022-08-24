# **************************************
# 004 - Виджет Label
# **************************************
# Andrey Kudlay (WebForMySelf), 2019
# ------------------------------------
# Writing by sgiman @ 2022, aug
#

from tkinter import *

# ---- window ----
win = Tk()
win.title('image')  # title
win.iconbitmap('../res/D-ICON.ico')  # icon
win.geometry('600x400+600+300')  # size & position
win.resizable(False, False)  # enable resize (width, height)
win['bg'] = 'blue'  # background

# LOGO IMAGE
img = PhotoImage(file='python-logo.png')
l_logo = Label(win, image=img)
l_logo.pack()

# LABEL 1
'''
l = Label(text="ABOUT:\n"
               "Строка 1\n"
               "Строка 2\n"
               "Строка 3\n"
               "Строка 4\n"
               "Строка 5",
          bg="blue",
          fg="#fff",
          font=("Comic Sans MS", 10, "bold"),
          justify=LEFT,
          width=20,
          height=6,
          anchor=SW)
'''

# LABEL 2
l1 = Label(win, text="ABOUT:\n"
                "Строка 1\n"
                "Строка 2\n"
                "Строка 3\n"
                "Строка 4\n"
                "Строка 5",
           bg="blue",
           fg="#fff",
           font=("Comic Sans MS", 10, "bold"),
           justify='center',
           height=7)

l1.pack()

l2 = Label(win, text="Copyright SCS @ 2022\n",
           bg="blue",
           fg="#fff",
           font=("Comic Sans MS", 10, "bold"),
           justify='center',
           width=20,
           height=6)

l2.pack()

win.mainloop()  # главный цикл событий окна win
