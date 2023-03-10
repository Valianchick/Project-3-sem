import pandas as pd
from faker import Faker
from faker.providers import BaseProvider
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
from tkinter.ttk import Style
import pandas as pd


class Computer: #класс компьюетр, в котором 9 параметров
    def __init__(self, code):
        self.code = code
        self.processor = None
        self.videocard = None
        self.ram = None
        self.screen = None
        self.inches = None
        self.hertz = None
        self.illumination = None
        self.price = None


    def __str__(self):
        comp1: str = f"Computer ID {self.code} \n" \
                    f"Processor {self.processor} \n" \
                    f"Videocard {self.videocard} \n" \
                    f"Ram {self.ram} \n" \
                    f"Screen {self.screen} \n" \
                    f"Inches {self.inches} \n" \
                    f"Hertz: {self.hertz} \n" \
                    f"Illumination: {self.illumination} \n" \
                    f"Price {self.price} \n"
        return comp1


class ComputerProvider(BaseProvider):
    PROCESSOR = ["Intel Celeron", "Intel Pentium",
                 "Amd Ryzen 3", "Amd Ryzen 5", "Amd Ryzen 7",
                 "Amd Ryzen 9", "Intel Core i3", "Intel Core i5",
                 "Intel Core i7", "Intel Core i9"]

    VIDEOCARD = ["GeoForce GTX 1050", "GeoForce GTX 1650", "GeoForce GTX 1660 Ti",
                 "GeoForce GTX 2060", "GeoForce GTX 3050", "GeoForce GTX 3050 Ti",
                 "GeoForce GTX 3060", "GeoForce GTX 3070", "GeoForce GTX 3080"]

    RAM = ["2", "4", "8", "16", "32"]

    INCHES = ["13", "14", "15"]

    SCREEN = ["Да", "нет"]

    HERTZ = ["144", "60"]

    ILLUMINATION = ["Да", "Нет"]

    fake_code = Faker("ru_RU")

    def fake_computer(self):
        computer = Computer(self.fake_code.bothify(text="???-###"))
        computer.processor = self.random_element(self.PROCESSOR)
        computer.videocard = self.random_element(self.VIDEOCARD)
        computer.ram = self.random_element(self.RAM)
        computer.inches = self.random_element(self.INCHES)
        computer.screen = self.random_element(self.SCREEN)
        computer.hertz = self.random_element(self.HERTZ)
        computer.illumination = self.random_element(self.ILLUMINATION)
        computer.price = self.random_int(15000, 40000)
        return computer


my_faker = Faker()
my_faker.add_provider(ComputerProvider)
data = []
for i in range(100000): #на каждой итерации создаем один фейковый ноутбук с помощью функции fake_computer
    fak = my_faker.fake_computer()
    dat = {"Computer ID": fak.code,
           "Processor": fak.processor,
           "Videocard": fak.videocard,
           "Ram": fak.ram,
           "Inches": fak.inches,
           "Screen": fak.screen,
           "Hertz": fak.hertz,
           "Illumination": fak.illumination,
           "Price": fak.price}
    data.append(dat)

df = pd.DataFrame(data=data) #таблица с данными о ноутбуках
print(df)

def variant(processor: str, videocard: str, ram: str, inches: str, hertz: str, price: str): #пользователь выбирает по 6 критериям ноутбук
    prc1 = int(price.split("-")[0]) #перевод в числовой вид
    prc2 = int(price.split("-")[1]) #перевод в числовой вид
    var = pd.DataFrame()
    for i, k in df.iterrows(): #на каждой итерации проверяется подходят ли параметры ноутбука под заданные параметры пользователем
        if ((videocard == k["Videocard"]) and (hertz == k["Hertz"]) #and (illumination == k["Illumination"])
                and (prc1 <= k["Price"] <= prc2) and (inches == k["Inches"])
                and (processor == k["Processor"]) and (ram == k["Ram"])):
            r = pd.DataFrame({"Computer ID": [k["Computer ID"]], "Processor": [k["Processor"]],
                              "Videocard": [k["Videocard"]], "Ram": [k["Ram"]],
                              "Inches": [k["Inches"]], "Screen": [k["Screen"]],
                              "Hertz": [k["Hertz"]], "Illumination": [k["Illumination"]], "Price": [k["Price"]]})
            var = pd.concat([var, r], ignore_index=True) #добавление строки в таблицу var
    #print(var)
    return var #возвращает созданную таблицу

def comp1(dat): #более приятный для глаз вывод
    note = [] #список для записи строк
    for i, k in dat.iterrows():
        note.append(f"ID компьютера: {k['Computer ID']} \n" +
              f"Процессор: {k['Processor']} \n" +
              f"Видеокарта: {k['Videocard']} \n" +
              f"Оперативная память: {k['Ram']} \n" +
              f"Дюймы: {k['Inches']} \n" +
              f"Герцы: {k['Hertz']} \n" +
              f"Цена: {k['Price']} \n" +
              f"Подсветка: {k['Illumination']} \n")
    return note



def base1():
    #проверка на заполненность ячеек
    if var1.get() == '' or var2.get() == '' or var3.get() == '' or var4.get() == '' or var5.get() == '' or var6.get() == '':
        messagebox.showinfo('Ошибка', 'Заполнены не все ячейки')
    else:
        base2 = comp1(variant(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()))
        wind = tk.Tk() #окошко
        wind.title('Информация о компьютерах')
        wind.geometry('1000x700')
        wind.configure(bg='light goldenrod')
        container = ttk.Frame(wind,
                              width=1000, height=700)
        canvas = Canvas(container,
                        width=800, height=700)
        scrollbar = ttk.Scrollbar(container,
                                  orient="vertical",
                                  command=canvas.yview) #скроллбар
        scrollable_frame = ttk.Frame(canvas, width=1000, height=700)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set,
                         background='light goldenrod')
        num = 1
        for i in range(len(base2)):
            ttk.Label(scrollable_frame,
                      text=base2[i] + "\n" + "\n",
                      wraplength=800, justify="center",
                      background='light goldenrod',
                      foreground="maroon",
                      font=("Times New Roman", 20)).grid(row=i, column=1)
            ttk.Label(scrollable_frame,
                      text=f"Вариант {num}" + "\n" + "\n",
                      wraplength=800, justify="center",
                      background='light goldenrod',
                      foreground="maroon",
                      font=("Times New Roman", 20)).grid(row=i, column=0)
            num += 1

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        wind.mainloop()

processors = ["Intel Celeron", "Intel Pentium",
                 "Amd Ryzen 3", "Amd Ryzen 5", "Amd Ryzen 7",
                 "Amd Ryzen 9", "Intel Core i3", "Intel Core i5",
                 "Intel Core i7", "Intel Core i9"]
videocards = ["GeoForce GTX 1050", "GeoForce GTX 1650", "GeoForce GTX 1660 Ti",
                 "GeoForce GTX 2060", "GeoForce GTX 3050", "GeoForce GTX 3050 Ti",
                 "GeoForce GTX 3060", "GeoForce GTX 3070", "GeoForce GTX 3080"]
ram_l = ["2", "4", "8", "16", "32"]
Inches_l = ["13", "14", "15"]
Herts_l = ["144", "60"]
price_list = ["15000-20000", "20000-25000", "25000-30000", "30000-35000", "35000-40000"]
#выборка для пользователя

#далее стандартное создание интерфейса с помощью tkinter
window = tk.Tk()
window.title('Computer')
window.geometry('853x700')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab',
                background="light goldenrod",
                font=('URW Gothic L','25','bold'))


note = Notebook(window)
frame1 = Frame(note, width= 1200, height=800)
frame1.configure(background="light goldenrod")
note.add(frame1, text= 'Выберите параметры ноутбука')

ttk.Label(frame1, text = "Процессор:", font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 1, padx = 10, pady = 25)
variable1 = StringVar()
var1 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable1,
                    font=("Times New Roman", 25))
var1['values'] = processors
var1.grid(column = 1, row = 1)
var1.current()


ttk.Label(frame1, text = "Видеокарта:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 2, padx = 10, pady = 25)
variable2 = StringVar()
var2 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable2,
                    font=("Times New Roman", 25))
var2['values'] = videocards
var2.grid(column = 1, row = 2)
var2.current()


ttk.Label(frame1, text = "Оперативная память:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 3, padx = 10, pady = 25)
variable3 = StringVar()
var3 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable3,
                    font=("Times New Roman", 25))
var3['values'] = ram_l
var3.grid(column = 1, row = 3)
var3.current()

ttk.Label(frame1, text = "Количество дюймов:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 4, padx = 10, pady = 25)
variable4 = StringVar()
var4 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable4,
                    font=("Times New Roman", 25))
var4['values'] = Inches_l
var4.grid(column = 1, row = 4)
var4.current()

ttk.Label(frame1, text = "Количество герц:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 5, padx = 10, pady = 25)

variable5 = StringVar()
var5 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable5,
                    font=("Times New Roman", 25))
var5['values'] = Herts_l
var5.grid(column = 1, row = 5)
var5.current()

ttk.Label(frame1, text = "Цена:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 6, padx = 10, pady = 25)

variable6 = StringVar()
var6 = ttk.Combobox(frame1, width = 22,
                    textvariable = variable6,
                    font=("Times New Roman", 25))
var6['values'] = price_list
var6.grid(column = 1, row = 6)
var6.current()

button1 = Button(frame1, text="Получить информацию",
                 font = ("Times New Roman", 25),
                background="mediumslateblue",
                 foreground ='linen', command=base1).grid(column = 1, row =7) #кнопочка для вывода информации о ноутбуках


note.pack(expand= True, fill=BOTH)
window.mainloop()
