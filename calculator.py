from tkinter import *
root=Tk()
root.title("Simple Calculator")
#create an entry widget
e=Entry(root, width=15, font=("Arial", 20), borderwidth=5)
#place it on the screen
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def but_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def but_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0, END)

def but_sub():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0, END)

def but_mul():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0, END)

def but_div():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0, END)

def but_poi():
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+".")

def but_eqa():
    second_number=e.get()
    e.delete(0, END)

    

    if math=="addition":
        e.insert(0, f_num+int(second_number))

    if math=="subtraction":
        e.insert(0, f_num-int(second_number))

    if math=="multiplication":
        e.insert(0, f_num*int(second_number))

    if math=="division":
        e.insert(0, f_num/int(second_number))


def but_cle():
    e.delete(0, END)

#create buttons
def create_buttons():
    button_1=Button(root, text="1", padx=15, pady=17, command=lambda: but_click(1))
    button_2=Button(root, text="2", padx=15, pady=17, command=lambda: but_click(2))
    button_3=Button(root, text="3", padx=15, pady=17, command=lambda: but_click(3))
    button_4=Button(root, text="4", padx=15, pady=17, command=lambda: but_click(4))
    button_5=Button(root, text="5", padx=15, pady=17, command=lambda: but_click(5))
    button_6=Button(root, text="6", padx=15, pady=17, command=lambda: but_click(6))
    button_7=Button(root, text="7", padx=15, pady=17, command=lambda: but_click(7))
    button_8=Button(root, text="8", padx=15, pady=17, command=lambda: but_click(8))
    button_9=Button(root, text="9", padx=15, pady=17, command=lambda: but_click(9))
    button_0=Button(root, text="0", padx=38, pady=17, command=lambda: but_click(0))
    button_add=Button(root, text="+", padx=14, pady=17, command=but_add)
    button_subtract=Button(root, text="-", padx=15, pady=17, command=but_sub)
    button_multiply=Button(root, text="x", padx=15, pady=17, command=but_mul)
    button_divide=Button(root, text="/", padx=15, pady=17, command=but_div)
    button_point=Button(root, text=".", padx=15.5, pady=17, command=but_poi)
    button_equal=Button(root, text="=", padx=20, pady=50, command=but_eqa)
    button_clear=Button(root, text="Clear", padx=11, pady=48, command=but_cle)

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0, columnspan=2)

    button_add.grid(row=1, column=3)
    button_subtract.grid(row=2, column=3)
    button_multiply.grid(row=3, column=3)
    button_divide.grid(row=4, column=3)
    button_point.grid(row=4, column=2)
    button_equal.grid(row=1, column=4, rowspan=2)
    button_clear.grid(row=3, column=4, rowspan=4)

create_buttons()

root.mainloop()