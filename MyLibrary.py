from tkinter import *
import sqlite3

vt = sqlite3.connect('database.db')
im = vt.cursor()
im.execute("create TABLE IF NOT EXISTS tablo (d1, d2,d3,d4)")
root = Tk()
root.title("My Library")
root.geometry("530x400")
saves = []
im.execute("SELECT * FROM tablo ")
data = im.fetchall()
print(data)
x = 0

for i in data:
    saves.append("                       ".join(i))
print(saves,"aa")

def add():
    global x
    d1 = no_entry.get()
    d2 = n_entry.get()
    d3 = s_entry.get()
    d4 = tel_entry.get()
    im.execute("INSERT INTO tablo (d1, d2,d3,d4) VALUES (?,?,?,?)", (d1, d2, d3, d4))
    x += 1
    listbox.insert(x,
                  d1 + " "*(40-len(d1)) + d2 +" "*(40-len(d2)) + d3 +" "*(45-len(d3))+ d4)
    saves.append([d1,d2,d3,d4])
    vt.commit()

def delete():
    name = listbox.get(ACTIVE)
    sel = listbox.curselection()
    for index in sel[::-1]:
        listbox.delete(index)
        saves.remove(saves[0])
    im.execute(f"DELETE FROM tablo WHERE d1=?", (name.split()[0],))
    vt.commit()


label = Label(root)
label.config(text="Book Name            Book No              Name        \t      Matrikel Number", bg="white", font=("Arial", 12))
label.place(x=1, y=1)

listbox = Listbox(root, width=110)
listbox.place(y=30)

for i in saves:
    listbox.insert(x, i)
    x += 1

number = Label(root, text="Book Name", font=("Arial", 12))
number.place(x=30, y=220)
no_entry = Entry(root)
no_entry.place(x=140, y=220)

name = Label(root, text="Book No", font=("Arial", 12))
name.place(x=30, y=250)
n_entry = Entry(root)
n_entry.place(x=140, y=250)

surname = Label(root, text="Student Name", font=("Arial", 12))
surname.place(x=30, y=280)
s_entry = Entry(root)
s_entry.place(x=140, y=280)

phone = Label(root, text="Matrikel Number", font=("Arial", 12))
phone.place(x=30, y=310)
tel_entry = Entry(root)
tel_entry.place(x=140, y=310)

add = Button(root, text="Add", font=("Verdana", 10), command=add)
add.place(x=300, y=230)

delete = Button(root, text="Delete", font=("Verdana", 10), command=delete)
delete.place(x=300, y=295)

mainloop()
