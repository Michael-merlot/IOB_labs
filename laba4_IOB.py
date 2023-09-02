import tkinter as tk
from tkinter import ttk


def calculate():
    message = message_entry.get()
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())
    t0 = int(t0_entry.get())

    # KSumm
    Summ = sum(ord(char) for char in message)
    k_summ_result = (a * Summ + b) % c

    # SummKodBukvOtkr
    Summ = 0
    t_prev = t0
    for char in message:
        x_i = ord(char)
        y_i = (x_i + t_prev) % c
        Summ += y_i
        t_prev = (a * t_prev + b) % c
    summ_kod_result = Summ

    ksumm_label.config(text=f"KSumm: {k_summ_result}")
    summ_kod_label.config(text=f"SummKodBukvOtkr: {summ_kod_result}")



app = tk.Tk()
app.title("Form4")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Заголовок
ttk.Label(frame, text="Входные данные").grid(row=0, columnspan=2, sticky=tk.W)
ttk.Label(frame, text="P: ").grid(row=1, column=0, sticky=tk.W)
message_entry = ttk.Entry(frame, width=20)
message_entry.grid(row=1, column=1)

ttk.Label(frame, text="a: ").grid(row=2, column=0, sticky=tk.W)
a_entry = ttk.Entry(frame, width=20)
a_entry.grid(row=2, column=1)

ttk.Label(frame, text="b: ").grid(row=3, column=0, sticky=tk.W)
b_entry = ttk.Entry(frame, width=20)
b_entry.grid(row=3, column=1)

ttk.Label(frame, text="c: ").grid(row=4, column=0, sticky=tk.W)
c_entry = ttk.Entry(frame, width=20)
c_entry.grid(row=4, column=1)

ttk.Label(frame, text="T0: ").grid(row=5, column=0, sticky=tk.W)
t0_entry = ttk.Entry(frame, width=20)
t0_entry.grid(row=5, column=1)

# Кнопка считать
ttk.Button(frame, text="Рассчитать", command=calculate).grid(row=6, columnspan=2)

# Заголовок результатов
ttk.Label(frame, text="Результат").grid(row=7, columnspan=2, sticky=tk.W)

# Результат
ksumm_label = ttk.Label(frame, text="KSumm: ")
ksumm_label.grid(row=8, columnspan=2, sticky=tk.W)

summ_kod_label = ttk.Label(frame, text="SummKodBukvOtkr: ")
summ_kod_label.grid(row=9, columnspan=2, sticky=tk.W)

app.mainloop()
