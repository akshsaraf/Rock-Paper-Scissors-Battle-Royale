import tkinter as tk
import random

root = tk.Tk()


def game():
    label.config(text="Rock, Paper or Scissor")
    deci = data.get().lower()

    comp_poss = random.choice(["rock", "paper", "scissors"])

    if deci == "rock":
        if comp_poss == "rock":
            label.config(text="IT WAS A TIE")
        elif comp_poss == "paper":
            label.config(text="Paper covers rock (You lost)")
        else:
            label.config(text="Rock destroys Scissors(You won)")

    elif deci == "paper":
        if comp_poss == "rock":
            label.config(text="Paper covers rock (You won)")
        elif comp_poss == "scissors":
            label.config(text="Scissors cuts Paper(You lost)")
        else:
            label.config(text="IT WAS A TIE")

    elif deci == "scissors":
        if comp_poss == "rock":
            label.config(text="Rock destroys Scissors (You lost)")
        elif comp_poss == "paper":
            label.config(text="IT WAS A TIE")
        else:
            label.config(text="Scissors cuts Paper(You won)")

    data.delete(0, tk.END)
    button.config(command=game)


data = tk.Entry(root)
data.pack()

label = tk.Label(root, text="Wanna Play a game?")
label.pack()

button = tk.Button(root, text="Yes")
button.pack()

button.config(command=game)

root.mainloop()