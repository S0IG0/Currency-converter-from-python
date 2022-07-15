from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
from get_dict_from_xml import get_dict_from_xml
from converter import converter
from render import *
from get_value_from_name import get_week_from_name, get_month_from_name, get_quarter_from_name, get_year_from_name


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.iconphoto(False, tk.PhotoImage(file='ruble.png'))
        self.title("Конвертер валют")

        self.data = get_dict_from_xml(*str(date.today()).split('-'))
        self.keys = list(self.data.keys())
        self.keys.sort()

        self.geometry('750x620')
        self.notebook = ttk.Notebook(self)
        self.tab_1 = tk.Frame(self.notebook)
        self.tab_2 = tk.Frame(self.notebook)

        self.fig = render('Доллар США')  #
        self.toolbarFrame = Frame(master=self.tab_2)
        self.plotFrame = Frame(master=self.tab_2)

        self.plotFrame.grid(row=2, column=0, columnspan=4)
        self.toolbarFrame.grid(row=3, column=0,  columnspan=4)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotFrame)
        self.toolbar = NavigationToolbar2Tk(self.canvas, window=self.toolbarFrame)
        self.canvas.get_tk_widget().pack()
        # self.canvas.draw()  #

        self.notebook.add(self.tab_1, text='Конвертер валют')
        self.notebook.add(self.tab_2, text='График')
        self.notebook.grid()

        self.label = tk.Label(
            self.tab_1,
            text="Выберите изначальную валюту",
            fg="black",
            width=25,
            height=2,
        )

        self.label_2 = tk.Label(
            self.tab_1,
            text="Выберите конечную валюту",
            fg="black",
            width=25,
            height=2
        )
        self.label_3 = tk.Label(
            self.tab_1,
            text="Введите кол-во:",
            fg="black",
            width=15,
            height=2
        )
        self.label_4 = tk.Label(
            self.tab_1,
            text="Результат:",
            fg="black",
            width=15,
            height=2
        )
        self.label_5 = tk.Label(
            self.tab_2,
            text="Валюта:",
            fg="black",
            width=15,
            height=2
        )
        self.label_6 = tk.Label(
            self.tab_2,
            text="Период:",
            fg="black",
            width=15,
            height=2
        )

        self.button = tk.Button(
            self.tab_1,
            text="Конвертация",
            width=10,
            height=2,
            bg="white",
            fg="black",
            command=self.clicked
        )

        self.button_2 = tk.Button(
            self.tab_1,
            text="Наоборот",
            width=10,
            height=2,
            bg="white",
            fg="black",
            command=self.clicked_2
        )

        self.button_3 = tk.Button(
            self.tab_2,
            text="Построить график",
            width=20,
            height=2,
            bg="white",
            fg="black",
            command=self.render_photo
        )

        self.button_4 = tk.Button(
            self.tab_2,
            text="Загрузить график",
            width=20,
            height=2,
            bg="white",
            fg="black",
            command=self.load_photo
        )

        self.entry = tk.Entry(self.tab_1, fg="black", bg="white", width=50)
        self.entry_2 = tk.Entry(self.tab_1, fg="black", bg="white", width=50)

        self.comboExample = ttk.Combobox(self.tab_1, values=self.keys + ['Российский рубль'], state='readonly')
        self.comboExample_2 = ttk.Combobox(self.tab_1, values=self.keys + ['Российский рубль'], state='readonly')

        self.label.grid(row=0, column=0)
        self.label_2.grid(row=1, column=0)
        self.comboExample.grid(row=0, column=1)
        self.comboExample_2.grid(row=1, column=1)
        self.label_3.grid(row=0, column=2)
        self.label_4.grid(row=1, column=2)
        self.entry.grid(row=0, column=3)
        self.entry_2.grid(row=1, column=3)
        self.button_2.grid(row=2, column=2)
        self.button.grid(row=2, column=3, columnspan=2, sticky='we')

        self.periods = ['Неделя', 'Месяц', 'Квартал', 'Год']
        self.functions = [get_week_from_name, get_month_from_name, get_quarter_from_name, get_year_from_name]

        self.comboExample_3 = ttk.Combobox(self.tab_2, values=self.keys, state='readonly')
        self.comboExample_4 = ttk.Combobox(self.tab_2, values=self.periods, state='readonly')

        self.label_5.grid(row=0, column=0)
        self.comboExample_3.grid(row=0, column=1)

        self.label_6.grid(row=1, column=0)
        self.comboExample_4.grid(row=1, column=1)

        self.button_3.grid(row=0, column=3, rowspan=2)

    def clicked(self):
        name_from = self.comboExample.get()
        name_to = self.comboExample_2.get()
        count = self.entry.get()

        if self.comboExample.current() != -1 and self.comboExample_2.current() != -1\
                and name_from != name_to and count.isdigit():
            self.entry.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(0, str(converter(name_from, name_to, int(count))) + ": " + name_to)

        else:
            self.entry.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(0, "FAIL")

    def clicked_2(self):
        index_1 = self.comboExample.get()
        index_2 = self.comboExample_2.get()

        print(index_1, index_2)

        self.comboExample.set(index_2)
        self.comboExample_2.set(index_1)

        name_from = self.comboExample.get()
        name_to = self.comboExample_2.get()
        count = self.entry.get()

        if self.comboExample.current() != -1 and self.comboExample_2.current() != -1 \
                and name_from != name_to and count.isdigit():
            self.entry.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(0, str(converter(name_from, name_to, int(count))) + ": " + name_to)

        else:
            self.entry.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(0, "FAIL")

    def render_photo(self):
        if self.comboExample_3.current() != -1 and self.comboExample_4.current() != -1:
            self.fig = render(name_value=self.comboExample_3.get(),
                              function=self.functions[self.comboExample_4.current()])

            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()

            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotFrame)
            self.toolbar = NavigationToolbar2Tk(self.canvas, window=self.toolbarFrame)
            self.canvas.get_tk_widget().pack()

    def load_photo(self):
        pass


root = Root()
root.mainloop()
