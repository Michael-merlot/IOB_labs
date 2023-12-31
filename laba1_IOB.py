import tkinter as tk
from tkinter import ttk
import random

# 14 вариант

def generate_password():
    username = username_entry.get()
    password = []

    uppercase_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lowercase_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    password.append(random.choice(uppercase_letters))
    password.append(random.choice(uppercase_letters))

    N = len(username)
    b3 = (N ** 2) % 10
    password.append(str(b3))

    password.append(str(random.randint(0, 9)))

    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']
    password.append(random.choice(special_characters))

    password.append(random.choice(lowercase_letters))

    password_label.config(text='Сгенерированный пароль: ' + ''.join(password))



window = tk.Tk()
window.title("Form1")

# Создание и расположение элементов интерфейса

username_label = ttk.Label(window, text="Введите идентификатор пользователя:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=1, columnspan=2, pady=10)

password_label = ttk.Label(window, text="Сгенерированный пароль: ")
password_label.grid(row=2, columnspan=2, pady=5)

window.mainloop()
