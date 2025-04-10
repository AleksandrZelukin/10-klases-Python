import tkinter as tk
from tkinter import messagebox

questions = {
    "Vārdnīca (dict)": [
        {
            "q": "Kā izveidot tukšu vārdnīcu Python valodā?",
            "options": ["[]", "()", "{}", "<>"],
            "answer": 2
        },
        {
            "q": 'Kā iegūt piekļuvi vārdnīcas atslēgas vērtībai? (d = {"vards": "Anna"})',
            "options": ['d["vards"]', "d.vards", 'd->"vards"', 'd.get("Anna")'],
            "answer": 0
        },
        # ... (Saīsina, turpinājums zemāk)
    ],
    "Darbs ar failiem": [
        {
            "q": 'Kā atvērt failu lasīšanai?',
            "options": ['open("fails.txt", "r")', 'open("fails.txt", "w")', 'open("fails.txt", "x")', 'open("fails.txt", "rw")'],
            "answer": 0
        },
        # ...
    ],
    "CSV datnes": [
        {
            "q": "Kura bibliotēka jāimportē darbam ar CSV?",
            "options": ["text", "csv", "fileio", "data"],
            "answer": 1
        },
        # ...
    ]
}

# Apvieno visus jautājumus vienā sarakstā
all_questions = []
for category, qs in questions.items():
    for q in qs:
        q["category"] = category
        all_questions.append(q)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python tests: Vārdnīcas, Faili, CSV")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, justify="left")
        self.question_label.pack(pady=20)

        self.option_vars = []
        self.option_buttons = []
        for i in range(4):
            var = tk.StringVar()
            btn = tk.Radiobutton(root, text="", variable=var, value=str(i), font=("Arial", 12), indicatoron=0, width=30, pady=5, command=self.select_answer)
            btn.pack(pady=2)
            self.option_vars.append(var)
            self.option_buttons.append(btn)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="gray")
        self.status_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Nākamais jautājums", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.q_index >= len(all_questions):
            messagebox.showinfo("Tests pabeigts", f"Tavs rezultāts: {self.score}/{len(all_questions)} pareizi.")
            self.root.destroy()
            return

        q = all_questions[self.q_index]
        self.correct_answer = q["answer"]
        self.question_label.config(text=f"{self.q_index + 1}. ({q['category']})\n{q['q']}")

        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].config(text=opt, state="normal")
            self.option_vars[i].set("")

        self.status_label.config(text="")
        self.next_button.config(state="disabled")

    def select_answer(self):
        selected = None
        for i, var in enumerate(self.option_vars):
            if self.option_buttons[i].select():
                selected = i
                break

        if selected is not None:
            is_correct = selected == self.correct_answer
            if is_correct:
                self.score += 1
                self.status_label.config(text="✅ Pareizi!", fg="green")
            else:
                pareizais = all_questions[self.q_index]["options"][self.correct_answer]
                self.status_label.config(text=f"❌ Nepareizi! Pareizā atbilde: {pareizais}", fg="red")

            for btn in self.option_buttons:
                btn.config(state="disabled")
            self.next_button.config(state="normal")

    def next_question(self):
        self.q_index += 1
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x400")
    app = QuizApp(root)
    root.mainloop()
