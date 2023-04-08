import sqlite3
from tkinter import *

# Создаем базу данных
conn = sqlite3.connect('hours_worked.db')
c = conn.cursor()

# Создаем таблицу
c.execute('''CREATE TABLE IF NOT EXISTS worked_hours
             (date text, hours real)''')

# Создаем графический интерфейс
root = Tk()
root.title("Отслеживание отработанных часов")


# Создаем функцию для добавления отработанных часов в базу данных
def add_hours():
    date = date_entry.get()
    hours = float(hours_entry.get())

    # Добавляем запись в базу данных
    c.execute("INSERT INTO worked_hours VALUES (?, ?)", (date, hours))
    conn.commit()

    # Очищаем поля ввода
    date_entry.delete(0, END)
    hours_entry.delete(0, END)


# Создаем функцию для отображения всех записей в базе данных
def show_hours():
    # Очищаем поле вывода
    output.delete('1.0', END)

    # Выбираем все записи из базы данных
    c.execute("SELECT * FROM worked_hours")
    rows = c.fetchall()

    # Выводим записи в поле вывода
    for row in rows:
        output.insert(END, f"{row[0]}: {row[1]} ч.\n")


# Создаем элементы интерфейса
date_label = Label(root, text="Дата (ДД.ММ.ГГГГ):")
date_entry = Entry(root)

hours_label = Label(root, text="Количество отработанных часов:")
hours_entry = Entry(root)

add_button = Button(root, text="Добавить", command=add_hours)
show_button = Button(root, text="Показать все записи", command=show_hours)

output_label = Label(root, text="Записи об отработанных часах:")
output = Text(root)

# Размещаем элементы интерфейса
date_label.grid(row=0, column=0)
date_entry.grid(row=0, column=1)

hours_label.grid(row=1, column=0)
hours_entry.grid(row=1, column=1)

add_button.grid(row=2, column=0)
show_button.grid(row=2, column=1)

output_label.grid(row=3, column=0)
output.grid(row=4, column=0, columnspan=2)

# Запускаем главный цикл
root.mainloop()

# Закрываем базу данных
conn.close()
