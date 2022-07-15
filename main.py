from tkinter import *
import tkinter.ttk as tkk
from get_dict_from_xml import get_dict_from_xml
from datetime import date


window = Tk()
window.title('Конвертор валют')
window.geometry('600x300')

tab_control = tkk.Notebook(window)
tab_1 = tkk.Frame(tab_control)
tab_2 = tkk.Frame(tab_control)

tab_control.add(tab_1, text="Вкладка №1")
tab_control.add(tab_2, text="Вкладка №2")

data = get_dict_from_xml(*str(date.today()).split('-'))

combo = tkk.Combobox(tab_1)
combo['value'] = list(data.keys())
combo.grid(column=0, row=0)

combo_2 = tkk.Combobox(tab_1)
combo_2['value'] = list(data.keys())
combo_2.grid(column=2, row=24)

txt = Entry(tab_1)
btn = Button(tab_1, text='Действие')
lbl = Label(tab_1, text='')

tab_control.pack(expand=1, fill='both')
window.mainloop()
