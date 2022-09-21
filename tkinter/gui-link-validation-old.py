# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:04:46 2022

@author: rajeshkanna
"""

import tkinter as tk
import webbrowser as wb


def Facebook():
    wb.open('facebook.com')


def Instagram():
    wb.open('instagram.com')


def Twitter():
    wb.open('twitter.com')


def Youtube():
    wb.open('youtube.com')


def Google():
    wb.open('google.com')


window = tk.Tk()
window.title('Browser')

google = tk.Button(window, text='Google', command=Google)
youtube = tk.Button(window, text='Youtube', bg='red', fg='white', command=Youtube)
twitter = tk.Button(window, text='Twitter', bg='powder blue', fg='white', command=Twitter)
Instagram = tk.Button(window, text='Instagram', bg='white', fg='black', command=Instagram)
facebook = tk.Button(window, text='Facebook', bg='blue', fg='white', command=Facebook)
facebook.pack()
Instagram.pack()
twitter.pack()
youtube.pack()
google.pack()

window.mainloop()