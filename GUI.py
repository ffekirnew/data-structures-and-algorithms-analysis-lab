# Names:    Fikernew Birhanu    Yohannes Bekele
# IDs:      UGR/9932/13         UGR/3361/13

import os
import tkinter
from tkinter import filedialog, messagebox
import html_validator

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"

# --------------------------------------------
def error_dialog(text):
    tkinter.messagebox.showerror('Error', text)

def start_acton():
    placeholder_label.config(text = '\n\n')
    file_location = tkinter.filedialog.askopenfilename()
    if not os.path.abspath(file_location).endswith('.html'):
        error_dialog("The file {} is not an HTML file.".format(file_location))
    else:
        isValid, last_line_number = html_validator.validator(file_location)
        if isValid:
            summary = "The HTML file is valid."
            placeholder_label.config(fg = GREEN, text = summary)
        else:
            summary = "The HTML file is not valid. \nCheck Line: " + str(last_line_number + 1) +'.'
            placeholder_label.config(fg = RED, text = summary)

screen = tkinter.Tk()
screen.minsize(300, 200)
screen.title('HTML Validator By Yohannes and Fikernew.')
screen.config(padx=50, pady=20, bg=PINK)

title_label = tkinter.Label(text="HTML\nValidator", bg=PINK, fg='white', font=('Arial', 20, ''), pady = 20)
title_label.pack()

start_button = tkinter.Button(text="Choose an HTML file...", bg='white', fg=RED, font=('Arial', 12, ''), pady = 10, highlightthickness=0, command=start_acton)
start_button.pack()

placeholder_label = tkinter.Label(text="\n\n", bg=PINK, fg='white', font=('Arial', 12, ''))
placeholder_label.pack()

screen.mainloop()