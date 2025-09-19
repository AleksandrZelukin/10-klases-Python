import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    """Проверка победителя"""
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    return None

def is_full():
    """Проверка заполненности поля"""
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

def click(row, col):
    global current_player, score_x, score_o
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            if winner == "X":
                score_x += 1
            else:
                score_o += 1
            update_score()
            messagebox.showinfo("Игра окончена", f"Игрок {winner} победил! 🎉")
            reset_board()
            return
        elif is_full():
            messagebox.showinfo("Игра окончена", "Ничья 🤝")
            reset_board()
            return

        # смена игрока
        current_player = "O" if current_player == "X" else "X"
        label_turn.config(text=f"Ход игрока: {current_player}")

        # если играем против компьютера
        if mode.get() == "AI" and current_player == "O":
            root.after(500, ai_move)  # задержка для "реализма"

def ai_move():
    """Ход компьютера"""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        click(row, col)

def reset_board():
    """Очистка поля"""
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    global current_player
    current_player = "X"
    label_turn.config(text=f"Ход игрока: {current_player}")

def update_score():
    """Обновление табло"""
    label_score.config(text=f"Счёт — X: {score_x} | O: {score_o}")

# окно
root = tk.Tk()
root.title("Крестики-нолики")

current_player = "X"
score_x = 0
score_o = 0
buttons = [[None for _ in range(3)] for _ in range(3)]

# режим игры
mode = tk.StringVar(value="2P")
frame_mode = tk.Frame(root)
frame_mode.grid(row=0, column=0, columnspan=3, pady=5)
tk.Label(frame_mode, text="Режим игры:", font=("Arial", 12)).pack(side="left")
tk.Radiobutton(frame_mode, text="2 игрока", variable=mode, value="2P").pack(side="left")
tk.Radiobutton(frame_mode, text="Против компьютера", variable=mode, value="AI").pack(side="left")

# табло
label_turn = tk.Label(root, text=f"Ход игрока: {current_player}", font=("Arial", 14))
label_turn.grid(row=1, column=0, columnspan=3, pady=5)

label_score = tk.Label(root, text="Счёт — X: 0 | O: 0", font=("Arial", 14), fg="blue")
label_score.grid(row=2, column=0, columnspan=3, pady=5)

# сетка кнопок
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda row=i, col=j: click(row, col))
        buttons[i][j].grid(row=i+3, column=j)

# запуск
root.mainloop()
