import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox

window = tk.Tk()
window.geometry('400x400')
window.title('Unit Converter')

font1 = font.Font(family = 'Segoe UI',size = '30')
font2 = font.Font(family = 'Segoe UI',size = '10')
font3 = font.Font(family = 'Segoe UI',size = '30')

main = tk.Label(window, text = 'Unit Converter',bg='#b19cd9')

window.mainloop()