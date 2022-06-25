import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox,StringVar
from tkinter.constants import UNITS
from tkinter import ttk

window = tk.Tk()
window.geometry('400x400')
window.title('Unit Converter')
window.configure(bg='#b19cd9')

font1 = font.Font(family = 'Segoe UI',size = '30')
font2 = font.Font(family = 'Segoe UI',size = '10')
font3 = font.Font(family = 'Segoe UI',size = '30')

def selected():
    pass

def from_func():
    pass

def to_func():
    pass



main = tk.Label(window, text = 'Unit Converter',bg='#b19cd9')
main['font'] = font1
main.place(relx = '0.5', rely = '0.1', anchor = 'center')

unit = tk.Label(window,text = 'Unit: ',bg = '#b19cd9', font  = font2)
unit.place(relx = '0.12', rely = '0.25', anchor = 'center')

n = StringVar()
unit_dropdown = ttk.Combobox(window,width = '35',textvariable = n)

unit_dropdown['values'] = ('Length',
                           'Weight',
                           'Time',
                           'Temperature')
unit_dropdown.place(relx = '0.50', rely = '0.25',anchor = 'center')
unit_dropdown.current()
unit_dropdown.bind('<<ComboboxSelected>>',selected)

label_from = tk.Label(window,text = 'From: ',bg = '#b19cd9',font=font2)
label_from.place(relx = '0.08',rely = '0.38')

f =StringVar()
from_dropdown = ttk.Combobox(window,width = '35',textvariable=f)

from_dropdown.place(relx = '0.50', rely = '0.41', anchor = 'center')
from_dropdown.current()
from_dropdown.bind('<<ComboboxSelected>>', from_func)

to = tk.Label(window,text = 'To: ',bg = '#b19cd9',font=font2)
to.place(relx = '0.08', rely = '0.53')

t  = StringVar()
to_dropdown = ttk.Combobox(window,width = 35, textvariable=t)
to_dropdown.place(relx = '0.50', rely = '0.56', anchor = 'center')
to_dropdown.current()
to_dropdown.bind('<<ComboboxSelected>>',to_func)

result_i = tk.Label(window,text = 'Result: ', bg = '#b19cd9' , font=font2)
result_i.place(relx = '0.08', rely = '0.69')
result = tk.Label(window, text = '',bg = 'white', width = 32,font=font2)
result.place(relx = '0.50', rely = '0.72',anchor = 'center')



window.mainloop()