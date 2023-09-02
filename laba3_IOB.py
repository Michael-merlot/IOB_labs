import tkinter as tk
from tkinter import ttk
import math
import random

# 29 вариант

def generate_password():
    P = float(prob_entry.get())
    V = float(velocity_entry.get()) * 60 * 24 * float(days_entry.get())

    alphabet = ''
    if var1.get():
        alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if var2.get():
        alphabet += 'abcdefghijklmnopqrstuvwxyz'
    if var3.get():
        alphabet += 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if var4.get():
        alphabet += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if var5.get():
        alphabet += '!@#$%^&*()-_=+'
    if var6.get():
        alphabet += '0123456789'

    A = len(alphabet)

    S_star = math.ceil(V / P)
    L = math.ceil(math.log(S_star, A))

    password = ''.join(random.choice(alphabet) for _ in range(L))

    result_label.config(text=f"Сгенерированный пароль: {password}")


app = tk.Tk()
app.title("Генератор паролей")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

prob_label = ttk.Label(frame, text="Вероятность подбора:")
prob_label.grid(row=0, column=0, sticky=tk.W)
prob_entry = ttk.Entry(frame, width=10)
prob_entry.grid(row=0, column=1)

velocity_label = ttk.Label(frame, text="Скорость перебора (в минуту):")
velocity_label.grid(row=1, column=0, sticky=tk.W)
velocity_entry = ttk.Entry(frame, width=10)
velocity_entry.grid(row=1, column=1)

days_label = ttk.Label(frame, text="Срок действия пароля (в днях):")
days_label.grid(row=2, column=0, sticky=tk.W)
days_entry = ttk.Entry(frame, width=10)
days_entry.grid(row=2, column=1)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

check1 = tk.Checkbutton(frame, text="Латинские большие", variable=var1)
check1.grid(row=3, column=0, sticky=tk.W)
check2 = tk.Checkbutton(frame, text="Латинские маленькие", variable=var2)
check2.grid(row=3, column=1, sticky=tk.W)
check3 = tk.Checkbutton(frame, text="Русские большие", variable=var3)
check3.grid(row=4, column=0, sticky=tk.W)
check4 = tk.Checkbutton(frame, text="Русские маленькие", variable=var4)
check4.grid(row=4, column=1, sticky=tk.W)
check5 = tk.Checkbutton(frame, text="Символы", variable=var5)
check5.grid(row=5, column=0, sticky=tk.W)
check6 = tk.Checkbutton(frame, text="Цифры", variable=var6)
check6.grid(row=5, column=1, sticky=tk.W)

gen_button = ttk.Button(frame, text="Генерировать пароль", command=generate_password)
gen_button.grid(row=6, columnspan=2)

result_label = ttk.Label(frame, text="Сгенерированный пароль:")
result_label.grid(row=7, columnspan=2, sticky=tk.W)

app.mainloop()
