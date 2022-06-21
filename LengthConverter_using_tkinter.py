#length converter using tkinter
from tkinter import *

window = Tk()
window.title("Length Converter")
window.geometry("500x300+550+355")
value = StringVar
def lengthconv():
     
    km = float(value.get())*1000
    mm = float(value.get())/1000
    cm = float(value.get())/100
    mile=float(value.get())*0.00062
    yard=float(value.get())*1.094
    inch=float(value.get())*39.37 
    foot=float(value.get())*3.281
    dm=float(value.get())*10