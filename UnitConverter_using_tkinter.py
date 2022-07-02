import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox,StringVar
from tkinter.constants import UNITS
from tkinter import ttk

window = tk.Tk()
window.iconbitmap(r'UC.ico')
window.geometry('400x400')
window.title('Unit Converter')
window.configure(bg='#b19cd9')
window.resizable(False,False)

font1 = font.Font(family = 'Segoe UI',size = '30')
font2 = font.Font(family = 'Segoe UI',size = '10')
font3 = font.Font(family = 'Segoe UI',size = '30')

number_from = StringVar()

def from_func(event):
    global result_from
    result_from = event.widget.get()

def to_func(event):
    global result_to
    result_to = event.widget.get()

def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror("Error",'Term not recognised')

    if result_from == 'Millimetre' and result_to == 'Centimetre':
        calculate = number1 * 0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millimetre' and result_to == 'Metre':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millimetre' and result_to == 'Kilometre':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Millimetre' and result_to == 'Inch':
        calculate = number1 * 0.03937008
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millimetre' and result_to == 'Yard':
        calculate = number1 * 0.00109361
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millimetre' and result_to == 'Foot':
        calculate = number1 * 0.00328084
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millimetre' and result_to == 'Mile':
        calculate = number1 * 1.6093 * (10)**6
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Millimetre':
        calculate = number1 / 0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Metre':
        calculate = number1 * 0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Kilometre':
        calculate = number1 * 0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Centimetre' and result_to == 'Inch':
        calculate = number1 * 0.3937008
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Yard':
        calculate = number1 * 0.01093613
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Foot':
        calculate = number1 * 0.0328084
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Centimetre' and result_to == 'Mile':
        calculate = number1 * 0.00000621
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Millimetre':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Centimetre':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Kilometre':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Metre' and result_to == 'Inch':
        calculate = number1 * 39.3700787
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Yard':
        calculate = number1 * 1.0936133
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Foot':
        calculate = number1 * 3.2808399
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metre' and result_to == 'Mile':
        calculate = number1 * 0.00062137
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Millimetre':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Centimetre':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Metre':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Kilometre' and result_to == 'Inch':
        calculate = number1 * 39370.0787
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Yard':
        calculate = number1 * 1093.6133
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Foot':
        calculate = number1 * 3280.8399
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilometre' and result_to == 'Mile':
        calculate = number1 * 0.62137119
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Millimetre':
        calculate = number1 * 25.4
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Centimetre':
        calculate = number1 * 2.54
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Metre':
        calculate = number1 * 0.0254
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Inch' and result_to == 'Kilometre':
        calculate = number1 * 0.0000254
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Yard':
        calculate = number1 * 0.02777778
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Foot':
        calculate = number1 * 0.08333333
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Mile':
        calculate = number1 * 0.00001578
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Millimetre':
        calculate = number1 * 304.8
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Centimetre':
        calculate = number1 * 30.48
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Metre':
        calculate = number1 * 0.3048
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Foot' and result_to == 'Inch':
        calculate = number1 * 12
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Yard':
        calculate = number1 * 0.33333333
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Kilometre':
        calculate = number1 * 0.0003048
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Mile':
        calculate = number1 * 0.00018939
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Millimetre':
        calculate = number1 * 914.4
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Centimetre':
        calculate = number1 * 91.44
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Metre':
        calculate = number1 * 0.9144
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Yard' and result_to == 'Inch':
        calculate = number1 * 36
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Kilometre':
        calculate = number1 * 0.0009144
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Foot':
        calculate = number1 * 3
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Mile':
        calculate = number1 * 0.00056818
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Millimetre':
        calculate = number1 * 1.6093 * (10)**6
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Centimetre':
        calculate = number1 * 160934.4
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Metre':
        calculate = number1 * 1609.344
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Inch':
        calculate = number1 * 63360
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Yard':
        calculate = number1 * 1760
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Foot':
        calculate = number1 * 5280
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Kilometre':
        calculate = number1 * 1.609344
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Milligram' and result_to == 'Gram':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Milligram' and result_to == 'Kilogram':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Milligram' and result_to == 'Ounce':
        calculate = number1 * 0.00003527
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Milligram' and result_to == 'Pound':
        calculate = number1 * 0.0000022
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Milligram' and result_to == 'Metric Ton':
        calculate = number1 * 10**-9
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Gram' and result_to == 'Milligram':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Gram' and result_to == 'Kilogram':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Gram' and result_to == 'Ounce':
        calculate = number1 * 0.03527396
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Gram' and result_to == 'Pound':
        calculate = number1 * 0.00220462
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Gram' and result_to == 'Metric Ton':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilogram' and result_to == 'Gram':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilogram' and result_to == 'Milligram':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilogram' and result_to == 'Ounce':
        calculate = number1 * 35.273962
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Kilogram' and result_to == 'Pound':
        calculate = number1 * 2.20462262
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kilogram' and result_to == 'Metric Ton':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))
    
    elif result_from == 'Ounce' and result_to == 'Milligram':
        calculate = number1 * 28349.5231
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Gram':
        calculate = number1 * 28.3495231
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Kilogram':
        calculate = number1 * 0.02834952
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Ounce' and result_to == 'Pound':
        calculate = number1 * 0.0625
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Metric Ton':
        calculate = number1 * 0.00002835
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Milligram':
        calculate = number1 * 453592.37
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Gram':
        calculate = number1 * 453.59237
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Kilogram':
        calculate = number1 * 0.45359237
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Pound' and result_to == 'Ounce':
        calculate = number1 * 16
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Metric Ton':
        calculate = number1 * 0.00045359
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metric Ton' and result_to == 'Milligram':
        calculate = number1 * 10**9
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metric Ton' and result_to == 'Gram':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metric Ton' and result_to == 'Kilogram':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
     
    elif result_from == 'Metric Ton' and result_to == 'Ounce':
        calculate = number1 * 35273.962
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Metric Ton' and result_to == 'Pound':
        calculate = number1 * 2204.62262
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Microsecond' and result_to == 'Millisecond':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Microsecond' and result_to == 'Second':
        calculate = number1 * 0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Microsecond' and result_to == 'Minute':
        calculate = number1 * 1.6667 * (10)**-8
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Microsecond' and result_to == 'Hour':
        calculate = number1 * 2.7778 * (10)**-10
        result.cget('text')
        result.configure(text=(calculate,result_to))   
    
    elif result_from == 'Millisecond' and result_to == 'Second':
        calculate = number1 * 0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millisecond' and result_to == 'Microsecond':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millisecond' and result_to == 'Minute':
        calculate = number1 * 0.00001667
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Millisecond' and result_to == 'Hour':
        calculate = number1 * 2.7778 * (10)**-7
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from == 'Second' and result_to == 'Microsecond':
        calculate = number1 * 1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Second' and result_to == 'Millisecond':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Second' and result_to == 'Minute':
        calculate = number1 * 0.01666667
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Second' and result_to == 'Hour':
        calculate = number1 * 0.00027778
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Minute' and result_to == 'Microsecond':
        calculate = number1 * 60000000 
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Minute' and result_to == 'Millisecond':
        calculate = number1 * 60000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Minute' and result_to == 'Second':
        calculate = number1 * 60
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Minute' and result_to == 'Hour':
        calculate = number1 * 0.01666667
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Hour' and result_to == 'Microsecond':
        calculate = number1 * 3.6000 * (10)**9 
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Hour' and result_to == 'Millisecond':
        calculate = number1 * 3600000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Hour' and result_to == 'Second':
        calculate = number1 * 3600
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Hour' and result_to == 'Minute':
        calculate = number1 * 60
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Celsius' and result_to == 'Fahrenheit':
        calculate = (number1 * 1.8) + 32
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Celsius' and result_to == 'Kelvin':
        calculate = number1 + 274.15
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Celsius':
        calculate = (number1 - 32) * 0.5555
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Fahrenheit' and result_to == 'Kelvin':
        calculate = number1 * 255.927778
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kelvin' and result_to == 'Fahrenheit':
        calculate = number1 - 457.87
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kelvin' and result_to == 'Celsius':
        calculate = number1 - 272.15
        result.cget('text')
        result.configure(text=(calculate,result_to))  

def selected(event):
    unit = event.widget.get()
    if unit == 'Length':
        from_dropdown['values'] = ('Millimetre',
                                   'Centimetre',
                                   'Metre',
                                   'Kilometre',
                                   'Inch',
                                   'Foot',
                                   'Yard',
                                   'Mile')

        to_dropdown['values'] = ('Millimetre',
                                 'Centimetre',
                                 'Metre',
                                 'Kilometre',
                                 'Inch',
                                 'Foot',
                                 'Yard',
                                 'Mile')

    elif unit == 'Mass':
        from_dropdown['values'] = ('Milligram',
                                   'Gram',
                                   'Kilogram',
                                   'Ounce',
                                   'Pound',
                                   'Metric Ton')

        to_dropdown['values'] = ('Milligram',
                                 'Gram',
                                 'Kilogram',
                                 'Ounce',
                                 'Pound',
                                 'Metric Ton')

    elif unit == 'Time':
        from_dropdown['values'] = ('Microsecond',
                                   'Millisecond',
                                   'Second',
                                   'Minute',
                                   'Hour')

        to_dropdown['values'] = ('Microsecond',
                                 'Millisecond',
                                 'Second',
                                 'Minute',
                                 'Hour')

    elif unit == 'Temperature':
        from_dropdown['values'] = ('Celsius',
                                   'Fahrenheit',
                                   'Kelvin')

        to_dropdown['values'] = ('Celsius',
                                   'Fahrenheit',
                                   'Kelvin')

main = tk.Label(window, text = 'Unit Converter',bg='#b19cd9')
main['font'] = font1
main.place(relx = '0.5', rely = '0.1', anchor = 'center')

unit = tk.Label(window,text = 'Unit: ',bg = '#b19cd9', font  = font2)
unit.place(relx = '0.12', rely = '0.32', anchor = 'center')

n = StringVar()
unit_dropdown = ttk.Combobox(window,width = '35',textvariable = n)

unit_dropdown['values'] = ('Length',
                           'Mass',
                           'Time',
                           'Temperature')
unit_dropdown.place(relx = '0.50', rely = '0.32',anchor = 'center')
unit_dropdown.current()
unit_dropdown.bind('<<ComboboxSelected>>',selected)

label_from = tk.Label(window,text = 'From: ',bg = '#b19cd9',font=font2)
label_from.place(relx = '0.08',rely = '0.41')

f =StringVar()
from_dropdown = ttk.Combobox(window,width = '35',textvariable=f)

from_dropdown.place(relx = '0.50', rely = '0.45', anchor = 'center')
from_dropdown.current()
from_dropdown.bind('<<ComboboxSelected>>', from_func)

num_from = tk.Label(window, text = 'Enter value: ',bg = '#b19cd9',font = font2)
num_from.place(relx = '0.08', rely = '0.19')
num_from = tk.Entry(window,width = 12,textvariable=number_from)
num_from.place(relx = '0.28', rely = '0.20')

answer = partial(answer,num_from)

to = tk.Label(window,text = 'To: ',bg = '#b19cd9',font=font2)
to.place(relx = '0.08', rely = '0.55')

t  = StringVar()
to_dropdown = ttk.Combobox(window,width = 35, textvariable=t)

to_dropdown.place(relx = '0.50', rely = '0.58', anchor = 'center')
to_dropdown.current()
to_dropdown.bind('<<ComboboxSelected>>',to_func)

result_i = tk.Label(window,text = 'Result: ', bg = '#b19cd9' , font=font2)
result_i.place(relx = '0.08', rely = '0.69')
result = tk.Label(window, text = '',bg = 'white', width = 32,font=font2)
result.place(relx = '0.50', rely = '0.72',anchor = 'center')

get_answer = tk.Button(window,text = 'Get Answer',font = font2,command=answer)
get_answer.place(relx = '0.42',rely = '0.78')



window.mainloop()