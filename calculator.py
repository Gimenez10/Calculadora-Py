from tkinter import *
from tkinter import ttk

def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

def clear():
    entry.delete(0, END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Erro")

def square_root():
    try:
        value = float(entry.get())
        result = value ** 0.5
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Erro")

def percentage():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Erro")

def backspace():
    current = entry.get()
    entry.delete(len(current)-1)

root = Tk()
root.title("Calculadora")
root.geometry("300x300")
root.configure(bg="darkgray")

entry = Entry(root, width=25, font=('Arial', 20), justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), relief="raised", width=6)
style.map('TButton', background=[('pressed', 'gray')], relief=[('pressed', 'sunken')])

# Botões numéricos
button_7 = ttk.Button(root, text="7", command=lambda: press(7), style='TButton')
button_8 = ttk.Button(root, text="8", command=lambda: press(8), style='TButton')
button_9 = ttk.Button(root, text="9", command=lambda: press(9), style='TButton')
button_4 = ttk.Button(root, text="4", command=lambda: press(4), style='TButton')
button_5 = ttk.Button(root, text="5", command=lambda: press(5), style='TButton')
button_6 = ttk.Button(root, text="6", command=lambda: press(6), style='TButton')
button_1 = ttk.Button(root, text="1", command=lambda: press(1), style='TButton')
button_2 = ttk.Button(root, text="2", command=lambda: press(2), style='TButton')
button_3 = ttk.Button(root, text="3", command=lambda: press(3), style='TButton')
button_0 = ttk.Button(root, text="0", command=lambda: press(0), style='TButton')

button_7.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
button_8.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
button_9.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
button_4.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
button_5.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
button_6.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
button_1.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
button_2.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
button_3.grid(row=3, column=2, sticky="ew", padx=5, pady=5)
button_0.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

# Botões de operação
button_equal = ttk.Button(root, text="=", command=evaluate, style='TButton')
button_clear = ttk.Button(root, text="C", command=clear, style='TButton')
button_decimal = ttk.Button(root, text=".", command=lambda: press("."), style='TButton')
button_square_root = ttk.Button(root, text="√", command=square_root, style='TButton')
button_backspace = ttk.Button(root, text="⌫", command=backspace, style='TButton')

button_clear.grid(row=2, column=3, sticky="ew", padx=5, pady=5)
button_equal.grid(row=5, column=1, rowspan=2, sticky="ew", padx=5, pady=5)
button_decimal.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
button_square_root.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
button_backspace.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

# Botões adicionais
button_add = ttk.Button(root, text="+", command=lambda: press("+"), style='TButton')
button_subtract = ttk.Button(root, text="-", command=lambda: press("-"), style='TButton')
button_multiply = ttk.Button(root, text="*", command=lambda: press("*"), style='TButton')
button_divide = ttk.Button(root, text="/", command=lambda: press("/"), style='TButton')
button_percentage = ttk.Button(root, text="%", command=percentage, style='TButton')


button_add.grid(row=3, column=3, sticky="ew", padx=5, pady=5)
button_subtract.grid(row=4, column=3, sticky="ew", padx=5, pady=5)
button_multiply.grid(row=5, column=3, sticky="ew", padx=5, pady=5)
button_divide.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
button_percentage.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

# Configurar redimensionamento responsivo
root.columnconfigure([0, 1, 2, 3], weight=1)
root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
root.mainloop()
