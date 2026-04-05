import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check_guess():
    global number, attempts
    guess = int(entry.get())
    attempts += 1

    if guess < number:
        result_label.config(text="Too Low!")
    elif guess > number:
        result_label.config(text="Too High!")
    else:
        result_label.config(text=f"Correct! It took you {attempts} attempts!")
        number = random.randint(1, 100)
        attempts = 0

# GUI
root = tk.Tk()
root.title("Guessing Game")

tk.Label(root, text="Guess a number (1-100):").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=check_guess).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()