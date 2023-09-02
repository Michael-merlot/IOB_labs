import tkinter as tk
from tkinter import ttk
import random
import string


# Функция для генерации пароля
def generate_password():
    username = username_entry.get()
    password = []

    password.append(random.choice(
        string.ascii_uppercase.replace('QWERTYUIOPLKJHGFDSAZXCVBNM', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')))
    password.append(random.choice(
        string.ascii_uppercase.replace('QWERTYUIOPLKJHGFDSAZXCVBNM', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')))

    N = len(username)
    b3 = (N ** 2) % 10
    password.append(str(b3))

    password.append(str(random.randint(0, 9)))

    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']
    password.append(random.choice(special_characters))

    password.append(random.choice(
        string.ascii_lowercase.replace('qwertyuiopasdfghjklzxcvbnm', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')))

    password_label.config(text='Сгенерированный пароль: ' + ''.join(password))


# Создание окна
window = tk.Tk()
window.title("Form1")

# Создание и расположение элементов интерфейса
username_label = ttk.Label(window, text="Идентификатор:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(window, text="Сформировать пароль", command=generate_password)
generate_button.grid(row=1, columnspan=2, pady=10)

password_label = ttk.Label(window, text="Сгенерированный пароль: ")
password_label.grid(row=2, columnspan=2, pady=5)

window.mainloop()
