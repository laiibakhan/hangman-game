import random
import os
from tkinter import *
from tkinter import messagebox

# ================== CONFIG ==================
score = 0
run = True

# Helper function to load images safely
def load_image(filename):
    """Load PNG image from same folder as the script"""
    try:
        path = os.path.join(os.path.dirname(__file__), filename)
        return PhotoImage(file=path)
    except Exception as e:
        print(f"⚠️ Missing image: {filename}  →  {e}")
        return None

# Load words
try:
    with open('words.txt', 'r', encoding='utf-8') as file:
        word_list = [line.strip().lower() for line in file if line.strip()]
    if not word_list:
        raise ValueError("words.txt is empty!")
except Exception as e:
    messagebox.showerror("Error", f"Cannot load words.txt\nError: {e}")
    exit()

# ================== MAIN GAME LOOP ==================
while run:
    root = Tk()
    root.geometry('920x740')
    root.title('HANGMAN')
    root.config(bg='#E7FFFF')
    root.resizable(False, False)

    count = 0
    win_count = 0

    selected_word = random.choice(word_list)

    # Hangman images area
    hang_label = Label(root, bg='#E7FFFF')
    hang_label.place(x=330, y=50)

    # Load hangman stages h1.png to h7.png
    hangman_images = []
    for i in range(1, 8):
        img = load_image(f"h{i}.png")
        hangman_images.append(img)

    if hangman_images[0]:
        hang_label.config(image=hangman_images[0])

    # Score
    score_label = Label(root, text=f"SCORE: {score}", bg="#E7FFFF", font=("arial", 26, "bold"))
    score_label.place(x=30, y=20)

    # Exit button
    exit_img = load_image("exit.png")
    if exit_img:
        Button(root, image=exit_img, bd=0, bg="#E7FFFF", activebackground="#E7FFFF",
               command=root.destroy).place(x=810, y=15)
    else:
        Button(root, text="Exit", font=("arial", 12), command=root.destroy).place(x=810, y=20)

    # Word blanks (centered)
    blanks = []
    word_length = len(selected_word)
    start_x = 460 - (word_length * 35)
    for i in range(word_length):
        lbl = Label(root, text="_", bg="#E7FFFF", font=("arial", 50), width=2)
        lbl.place(x=start_x + i*70, y=420)
        blanks.append(lbl)

    # Load all letter images a.png to z.png
    letter_images = {}
    for let in 'abcdefghijklmnopqrstuvwxyz':
        letter_images[let] = load_image(f"{let}.png")

    # ================== CHECK FUNCTION ==================
    def check(letter, btn):
        global count, win_count, score, run

        btn.destroy()

        if letter in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == letter:
                    blanks[i].config(text=letter.upper())
                    win_count += 1

            if win_count == len(selected_word):
                score += 1
                ans = messagebox.askyesno('You Won!', f'Excellent!\nScore: {score}\nPlay Again?')
                if ans:
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            if count < len(hangman_images) and hangman_images[count]:
                hang_label.config(image=hangman_images[count])

            if count == 6:
                ans = messagebox.askyesno('Game Over', 
                    f'You Lost!\nThe word was: {selected_word.upper()}\nPlay Again?')
                if ans:
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    # ================== KEYBOARD (Clean Grid) ==================
    keyboard_frame = Frame(root, bg='#E7FFFF')
    keyboard_frame.place(x=70, y=560)

    rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for r, row_letters in enumerate(rows):
        for c, let in enumerate(row_letters):
            img = letter_images.get(let)
            if img:
                btn = Button(keyboard_frame, image=img, bd=0, bg='#E7FFFF',
                             activebackground='#E7FFFF')
                btn.grid(row=r, column=c, padx=5, pady=6)
                btn.config(command=lambda l=let, b=btn: check(l, b))

    root.mainloop()