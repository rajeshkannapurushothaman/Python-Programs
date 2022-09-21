# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:07:05 2022

@author: rajeshkanna
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:04:46 2022

@author: rajeshkanna
"""

from tkinter import *
import requests
import pandas as pd
import sys, os
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter import Tk, font



def close_window():
    linkui.destroy()
    

# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(title="Open a Excel File", filetype=(("xlxs files", ".*xlsx"),
("All Files", "*.xlsx")))
    text1.delete(0, END)
    text1.insert(END, filename)
    my_string_var.set(' ')
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)


def validation():
    my_string_var.set('Please Wait...')
    if 'Browse' in text1.get() or text1.get() == '' or text1.get() == None:
        messagebox.showerror("Error", "Browse a xlsx file")
        my_string_var.set(' ')
    else:
        excel_validation()

def excel_validation():
    #label3.config(text='Please Wait...')
    
    
    df = pd.read_excel(text1.get())
    
    logtext = ''
    
    for url in df['Website URL']:
    
       try:
           print('Processing -- '+ url.strip() + '\n')
           label3['text']='Processing -- '+ url.strip()
           response= requests.get(url.strip())
           if response.status_code >= 200 and response.status_code < 400:
               logtext = logtext + '\n'  + 'Success! -- ' + url
           else:
               logtext = logtext + '\n' + 'Failed to Connect! -- ' + url
       except Exception as err:
           logtext = logtext + '\n' + 'Failed to Connect! - It may be a proxy issue -- ' + url
           
    with open(os.path.splitext(text1.get())[0] + '-log.txt', 'w') as my_log_file:
        my_log_file.write(logtext)
        my_log_file.close()
    
    clear = lambda: os.system('cls')
    clear()
    
    print('\n\n***** Process Completed *****\n\n')
    my_string_var.set('Process Completed')
    
    #label3.config(text='Process Completed!')


# GUI creation part

linkui = Tk()
linkui.geometry('600x300')
linkui.title('Website Link Validation')
linkui['background'] = '#F0F0F0'
font.families()


spacing1 = Label(linkui, bg="#F0F0F0")
spacing1.pack()

label1 = Label(linkui, font=("Malgun Gothic Semilight", 16, "normal"), text='Website URL Validation', fg="#03A9F4")
label1.pack()

spacing2 = Label(linkui, bg="#F0F0F0")
spacing2.pack()

text1 = Entry(linkui, fg="#455364")
text1.insert(END, 'Browse excel File')
text1.place(x=85, y=120, height=22, width=360)

browsebtn = Button(linkui, text='Browse',command=browseFiles, borderwidth=1, border=1, fg="#03A9F4")
browsebtn.place(x=465, y=120, height=25, width=70)

google = Button(linkui, fg="#03A9F4", text='Validate', borderwidth=1, border=1, command=validation)
google.place(x=180, y=190, height=25, width=70)

button_exit = Button(linkui,
                     text = "Exit",
                     fg="#03A9F4",
                     command = close_window, borderwidth=1, border=1)
button_exit.place(x=290, y=190, height=25, width=70)

label2 = Label(linkui, height=1, width=25, fg="#03A9F4", text='Version: 1.0.0.0')
label2.place(x=405, y=265)

my_string_var = StringVar()


label3 = Label(linkui, height=1, width=25, fg="#03A9F4", textvariable = my_string_var)
label3.place(x=180, y=240)


linkui.mainloop()