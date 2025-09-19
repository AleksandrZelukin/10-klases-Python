import tkinter as tk
import random

# варианты
choices = ["Камень", "Ножницы", "Бумага"]

# логика игры
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
         (user_choice == "Бумага" and computer_choice == "Камень"):
        result = "Вы победили!"
    else:
        result = "Компьютер победил!"

    label_result.config(
        text=f"Вы: {user_choice}\nКомпьютер: {computer_choice}\n\n{result}"
    )

# создаём окно
root = tk.Tk()
root.title("Камень, ножницы, бумага")
root.geometry("300x250")

label_title = tk.Label(root, text="Выберите ход:", font=("Arial", 14))
label_title.pack(pady=10)

# кнопки
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text="Камень", width=10, command=lambda: play("Камень"))
btn_rock.grid(row=0, column=0, padx=5)

btn_scissors = tk.Button(frame_buttons, text="Ножницы", width=10, command=lambda: play("Ножницы"))
btn_scissors.grid(row=0, column=1, padx=5)

btn_paper = tk.Button(frame_buttons, text="Бумага", width=10, command=lambda: play("Бумага"))
btn_paper.grid(row=0, column=2, padx=5)

# результат
label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=20)

root.mainloop()
