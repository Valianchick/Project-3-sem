def variant(processor: str, videocard: str, ram: str, inches: str, hertz: str, price: str):
    prc1 = int(price.split("-")[0])
    prc2 = int(price.split("-")[1])
    var = pd.DataFrame()
    for i, k in df.iterrows():
        if ((videocard == k["Videocard"]) and (hertz == k["Hertz"]) #and (illumination == k["Illumination"])
                and (prc1 <= k["Price"] <= prc2) and (inches == k["Inches"])
                and (processor == k["Processor"]) and (ram == k["Ram"])):
            r = pd.DataFrame({"Computer ID": [k["Computer ID"]], "Processor": [k["Processor"]],
                              "Videocard": [k["Videocard"]], "Ram": [k["Ram"]],
                              "Inches": [k["Inches"]], "Screen": [k["Screen"]],
                              "Hertz": [k["Hertz"]], "Illumination": [k["Illumination"]], "Price": [k["Price"]]})
            var = pd.concat([var, r], ignore_index=True)
    #print(var)
    return var

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
