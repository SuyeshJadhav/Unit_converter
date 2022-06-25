import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.geometry('400x400')
window.title('Unit Converter')
window.configure(bg='#b19cd9')

font1 = font.Font(family = 'Segoe UI',size = '30')
font2 = font.Font(family = 'Segoe UI',size = '10')
font3 = font.Font(family = 'Segoe UI',size = '30')

main = tk.Label(window, text = 'Unit Converter',bg='#b19cd9')
main['font'] = font1
main.place(relx = '0.5', rely = '0.1', anchor = 'center')

unit = tk.Label(window,text = 'Unit: ',bg = '#b19cd9')
unit['font'] = font2
unit.place(relx = '0.08', rely = '0.22')

unit_dropdown = ttk.Combobox(window,width = '35',textvariable = n)

unit_dropdown['values'] = ('Length') 


window.mainloop()