from tkinter import *
import sqlite3

conn = sqlite3.connect('db/tk_base.db')
cur = conn.cursor()

def insert_data():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    national = national_entry.get()
    cur.execute('''
    INSERT INTO users (id, name, age, national) VALUES (?, ?, ?, ?)
    ''', (id, name, age, national))
    conn.commit()
    print('Data added!')
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    national_entry.delete(0, END)
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)

app = Tk()
app.title('Add users')
app.geometry('400x300')
app.resizable(False, False)

id_label = Label(app, text = 'ID: ')
id_label.pack(pady = 5)
id_entry = Entry(app)
id_entry.pack(pady=5)

name_label = Label(app, text="NAME:")
name_label.pack(pady=5)
name_entry = Entry(app)
name_entry.pack(pady=5)

age_label = Label(app, text="AGE:")
age_label.pack(pady=5)
age_entry = Entry(app)
age_entry.pack(pady=5)

national_label = Label(app, text="NATIONAL:")
national_label.pack(pady=5)
national_entry = Entry(app)
national_entry.pack(pady=5)

submit_button = Button(app, text = 'Add', command = insert_data)
submit_button.pack(pady=20)

app.mainloop()