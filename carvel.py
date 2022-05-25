from tkinter import *
from tkinter.messagebox import showinfo

import auto
from db import Database
from tkinter import ttk
from tkinter import messagebox
import itertools
import tkinter as tk

db = Database('orders.db')


def populate_list():
    my_listbox.delete(0, END)
    for row in db.fetch():
        my_listbox.insert(END, row)


def add_qty():
    db.insert(qty_text.get())
    my_listbox.delete(0, END)
    my_listbox.insert(END, qty_text.get())
    # populate_list()


def select_item(event):
    try:
        global selected_item
        global index
        index = my_listbox.curselection()[0]
        selected_item = my_listbox.get(index)

        qty_entry.delete(0, END)
        qty_entry.insert(END, selected_item[3])

    except IndexError:
        pass


def remove_qty():
    response = messagebox.askokcancel("Item removing",
                                      "Are you sure you want to remove this item?")
    if response == 1:
        db.remove(selected_item[0])
        clear_text()
        populate_list()
    else:
        return


def update_qty():
    db.update(selected_item[0], selected_item[1], selected_item[2], qty_entry.get())
    refresh_item()
    populate_list()
    my_listbox.see(index + 1)
    my_listbox.select_set(index)
    my_listbox.activate(index)


def clear_text():
    qty_entry.delete(0, END)


def refresh_item():
    i = 0
    for row in db.fetch():
        if row[3] != '0':
            i = i + 1
            if i > 37:
                messagebox.showwarning(title='invalid',
                                       message='out of range, please clear the all quantities to continue')
    change_text(i)


root = Tk()
root.title('carvel Auto order')
root.iconbitmap('C:/Users/28696/Desktop/carvel auto/carvel.ico')
root.geometry("450x450")

my_listbox = Listbox(root, height=10, width=50, font=('bold', 12))
my_listbox.grid(row=0, column=0, columnspan=10, rowspan=1, padx=20, pady=20, sticky='nwes')

scrollbar = tk.Scrollbar(root, orient='vertical', command=my_listbox.yview)
my_listbox['yscrollcommand'] = scrollbar.set
scrollbar.grid(column=10, row=0, sticky='ns')
my_listbox.bind('<<ListboxSelect>>', select_item)

qty_text = tk.StringVar()
qty_label = Label(root, text='Quantity', font=('bold', 12))
qty_label.grid(row=2, column=0, sticky=W)
qty_entry = Entry(root, width=8, borderwidth=2, bg="white", fg="black")
qty_entry.grid(row=2, column=1, padx=10, pady=15)


def button_click(number):
    current = qty_entry.get()
    qty_entry.delete(0, END)
    qty_entry.insert(0, str(current) + str(number))


def button_clear_quantity():
    response = messagebox.askokcancel("reset quantity to 0",
                                      "Do you want to reset all quantity to 0?")
    if response == 1:
        db.clear_quantity()
        refresh_item()
        populate_list()
    else:
        return


def button_save():
    response = messagebox.askokcancel("Order confirmation",
                                      "Do you want to save these orders?")
    Label(root, text="                 "
                     "                    ").grid(row=6, column=1, columnspan=3)
    if response == 1:
        Label(root, text="Save successfully").grid(row=6, column=1, columnspan=3)
        auto = open('auto.txt', 'w')
        for row in db.fetch():
            if row[3] != 0:
                auto.writelines(str(row[2]))
                auto.write("\n")
                auto.writelines(str(row[3]))
                auto.write("\n")
                auto.write("\n\n")
        auto.close()
    else:
        Label(root, text="Save cancelled").grid(row=6, column=1, columnspan=3)


def button_edit():
    top = Toplevel()
    top.title('Edit the order')
    btn2 = Button(top, text="close window",
                  command=top.destroy).grid(row=4, column=1, columnspan=3)


button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_clear = Button(root, text="Clear All quantity", padx=12, pady=10, command=button_clear_quantity)
button_save = Button(root, text="Save", padx=9, pady=10, command=button_save)
btn = button_edit = Button(root, text="Edit order", padx=9, pady=10, command=button_edit)


def execute():
    auto.autofill()


button_fill = Button(root, text="Auto fill", padx=14, pady=10, command=execute)
button_fill.grid(row=4, column=5)

# put the buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=4, column=3)
button_5.grid(row=4, column=4)
button_edit.grid(row=3, column=5)
button_6.grid(row=3, column=0)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)
button_0.grid(row=3, column=4)
button_clear.grid(row=5, column=0, columnspan=2)
button_save.grid(row=5, column=4)

button_quit = Button(root, text="Exit "
                                "Program", padx=20, pady=10, command=root.quit)
button_quit.grid(row=5, column=2, columnspan=2)

add_btn = Button(root, text="Add Data", command=add_qty, fg="#800000", bg="white")
add_btn.grid(row=2, column=4)

remove_btn = Button(root, text="Remove", command=remove_qty, fg="#800000", bg="white")
remove_btn.grid(row=2, column=5)

update_btn = Button(root, text="Update", command=update_qty, fg="#800000", bg="white")
update_btn.grid(row=2, column=3)

clear_btn = Button(root, text="⌫Clear", command=clear_text, fg="#800000", bg="white")
clear_btn.grid(row=2, column=2)

global my_lable


def change_text(items):
    if items != 0:
        my_lable.configure(text=str(items) + "/37")
    else:
        my_lable.configure(text="0/37")


my_lable = Label(root, text='')
my_lable.grid(row=6, column=5)
populate_list()

root.mainloop()
