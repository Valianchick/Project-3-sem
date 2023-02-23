window = tk.Tk()
window.title('Computer')
window.geometry('900x700')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab',
                background="light goldenrod",
                font=('URW Gothic L','25','bold'))


note = Notebook(window)
frame1 = Frame(note, width= 1200, height=800)
frame1.configure(background="light goldenrod")
note.add(frame1, text= 'Выбор ноутбука')


ttk.Label(frame1, text = "Процессор:", font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 1, padx = 10, pady = 25)
variable1 = StringVar()
var1 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable1,
                    font=("Times New Roman", 20))
var1['values'] = processors
var1.grid(column = 1, row = 1)
var1.current()


ttk.Label(frame1, text = "Видеокарта:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 2, padx = 10, pady = 25)
variable2 = StringVar()
var2 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable2,
                    font=("Times New Roman", 20))
var2['values'] = videocards
var2.grid(column = 1, row = 2)
var2.current()


ttk.Label(frame1, text = "Оперативная память:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 3, padx = 10, pady = 25)
variable3 = StringVar()
var3 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable3,
                    font=("Times New Roman", 20))
var3['values'] = ram_l
var3.grid(column = 1, row = 3)
var3.current()

ttk.Label(frame1, text = "Количество дюймов:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 4, padx = 10, pady = 25)
variable4 = StringVar()
var4 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable4,
                    font=("Times New Roman", 20))
var4['values'] = Inches_l
var4.grid(column = 1, row = 4)
var4.current()

ttk.Label(frame1, text = "Количество герц:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 5, padx = 10, pady = 25)
variable5 = StringVar()
var5 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable5,
                    font=("Times New Roman", 20))
var5['values'] = Herts_l
var5.grid(column = 1, row = 5)
var5.current()

ttk.Label(frame1, text = "Цена:",
          font = ("Times New Roman", 25),
          background = 'light goldenrod',
          foreground ="mediumslateblue").grid(column = 0,
		row = 6, padx = 10, pady = 25)
variable6 = StringVar()
var6 = ttk.Combobox(frame1, width = 20,
                    textvariable = variable6,
                    font=("Times New Roman", 20))
var6['values'] = price_list
var6.grid(column = 1, row = 6)
var6.current()

button1 = Button(frame1, text="Получить информацию",
                 font = ("Times New Roman", 25),
                background="mediumslateblue",
                 foreground ='linen', command=base1).grid(column = 1, row =7)


note.pack(expand= True, fill=BOTH)
window.mainloop()
