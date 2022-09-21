# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:12:45 2022

@author: rajeshkanna
"""

from tkinter import *


# def click func
def click():
    # Getting the text info as an int() & Error handling
    try:
        text_info_1 = float(text1.get())
        text_info_2 = float(text2.get())
    except Exception as e:
        text1.delete(0, END)
        text2.delete(0, END)
        text3.delete(0, END)
        text3.insert(0, f'Error: {e}')
        return
    # actual part of the func
    text3.delete(0, END)
    text3.insert(0, text_info_1 + text_info_2)

# Gui Config
root = Tk()
root.geometry('300x400')
root.title('Poop')

# The actual gui
label1 = Label(root, text='Write something!')
label1.pack()

spacing1 = Label(root)
spacing1.pack()

text1 = Entry(root)
text1.pack(ipadx=20)

spacing2 = Label(root, text='+')
spacing2.pack()

text2 = Entry(root)
text2.pack(ipadx=20)

spacing3 = Label(root)
spacing3.pack()

button = Button(root, text='Click me!', command=click)
button.pack()

spacing4 = Label(root)
spacing4.pack()

text3 = Entry(root)
text3.pack(ipadx=60)

# Making the gui run
root.mainloop()