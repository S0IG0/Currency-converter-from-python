import random
import time
import tkinter as tk
from tkinter import ttk
from get_dict_from_xml import get_dict_from_xml
from datetime import date
from converter import converter
from render import *
from get_value_from_name import get_week_from_name, get_month_from_name, get_quarter_from_name, get_year_from_name



# from PIL import Image, ImageTk


def clicked():
    name_from = comboExample.get()
    name_to = comboExample_2.get()
    count = entry.get()

    if comboExample.current() != -1 and comboExample_2.current() != -1 and name_from != name_to and count.isdigit():
        entry.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        entry_2.insert(0, str(converter(name_from, name_to, int(count))) + ": " + name_to)

    else:
        entry.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        entry_2.insert(0, "FAIL")


def clicked_2():
    index_1 = comboExample.get()
    index_2 = comboExample_2.get()

    print(index_1, index_2)

    comboExample.set(index_2)
    comboExample_2.set(index_1)

    name_from = comboExample.get()
    name_to = comboExample_2.get()
    count = entry.get()

    if comboExample.current() != -1 and comboExample_2.current() != -1 and name_from != name_to and count.isdigit():
        entry.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        entry_2.insert(0, str(converter(name_from, name_to, int(count))) + ": " + name_to)

    else:
        entry.delete(0, tk.END)
        entry_2.delete(0, tk.END)
        entry_2.insert(0, "FAIL")


def render_photo():
    if comboExample_3.current() != -1 and comboExample_4.current() != -1:
        f = render(name_value=comboExample_3.get(), function=functions[comboExample_4.current()])
        canvas = FigureCanvasTkAgg(f, tab_2)
        canvas.get_tk_widget().grid(row=3, column=3)
        # toolbar = NavigationToolbar2Tk(canvas, window=window)
        toolbar = NavigationToolbar2Tk(canvas, window=tab_2)
        # canvas._tkcanvas.grid()
        # toolbar.pack()
        # toolbar.grid(row=4, column=1)

        #
        # toolbar.update()
        # tab_2.update()
        # window.update()



def load_photo():
    obj = tk.PhotoImage(file=r'Data/foo.png')
    # canvas.create_image(0, 40, anchor='nw', image=obj)

    tab_2.update()
    window.update()


data = get_dict_from_xml(*str(date.today()).split('-'))
keys = list(data.keys())
keys.sort()

window = tk.Tk()
window.geometry('1000x1000')

notebook = ttk.Notebook(window)
tab_1 = tk.Frame(notebook)
tab_2 = tk.Frame(notebook)

#################################################
# fig = render('Доллар США')                      #
# canvas = FigureCanvasTkAgg(fig, master=tab_2)   #
# canvas.get_tk_widget().grid(row=3, column=3, columnspan=2)                 #
# canvas.draw()                                   #
#################################################

notebook.add(tab_1, text='Конвертер валют')
notebook.add(tab_2, text='График')
notebook.pack()

label = tk.Label(
    tab_1,
    text="Выберите изначальную валюту",
    fg="black",
    width=25,
    height=2
)

label_2 = tk.Label(
    tab_1,
    text="Выберите конечную валюту",
    fg="black",
    width=25,
    height=2
)
label_3 = tk.Label(
    tab_1,
    text="Введите кол-во:",
    fg="black",
    width=15,
    height=2
)
label_4 = tk.Label(
    tab_1,
    text="Результат:",
    fg="black",
    width=15,
    height=2
)
label_5 = tk.Label(
    tab_2,
    text="Валюта:",
    fg="black",
    width=15,
    height=2
)
label_6 = tk.Label(
    tab_2,
    text="Период:",
    fg="black",
    width=15,
    height=2
)

button = tk.Button(
    tab_1,
    text="Конвертация",
    width=10,
    height=2,
    bg="white",
    fg="black",
    command=clicked
)

button_2 = tk.Button(
    tab_1,
    text="Наоборот",
    width=10,
    height=2,
    bg="white",
    fg="black",
    command=clicked_2
)

button_3 = tk.Button(
    tab_2,
    text="Построить график",
    width=20,
    height=2,
    bg="white",
    fg="black",
    command=render_photo
)

button_4 = tk.Button(
    tab_2,
    text="Загрузить график",
    width=20,
    height=2,
    bg="white",
    fg="black",
    command=load_photo
)

entry = tk.Entry(tab_1, fg="black", bg="white", width=50)
entry_2 = tk.Entry(tab_1, fg="black", bg="white", width=50)

comboExample = ttk.Combobox(tab_1, values=keys + ['Российский рубль'], state='readonly')
comboExample_2 = ttk.Combobox(tab_1, values=keys + ['Российский рубль'], state='readonly')

label.grid(row=0, column=0)
label_2.grid(row=1, column=0)
comboExample.grid(row=0, column=1)
comboExample_2.grid(row=1, column=1)
label_3.grid(row=0, column=2)
label_4.grid(row=1, column=2)
entry.grid(row=0, column=3)
entry_2.grid(row=1, column=3)
button_2.grid(row=2, column=2)
button.grid(row=2, column=3, columnspan=2, sticky='we')

periods = ['Неделя', 'Месяц', 'Квартал', 'Год']
functions = [get_week_from_name, get_month_from_name, get_quarter_from_name, get_year_from_name]

comboExample_3 = ttk.Combobox(tab_2, values=keys, state='readonly')
comboExample_4 = ttk.Combobox(tab_2, values=periods, state='readonly')

# canvas = tk.Canvas(tab_2, width=500, height=500)

label_5.grid(row=0, column=0)
comboExample_3.grid(row=0, column=1)

label_6.grid(row=1, column=0)
comboExample_4.grid(row=1, column=1)

button_3.grid(row=0, column=3, rowspan=2)
button_4.grid(row=0, column=4, rowspan=2)
# canvas.grid(row=3, column=3, columnspan=2)

window.mainloop()



