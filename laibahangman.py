import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg='#E7FFFF')
    
    # Force window to popup on MacOS
    root.lift()
    root.attributes('-topmost', True)
    root.after(500, lambda: root.attributes('-topmost', False))
    root.focus_force()

    count = 0
    win_count = 0

    categories = {
        "Fruits": ["apple", "banana", "grape", "orange", "mango", "peach", "cherry", "melon", "lemon", "papaya", "watermelon"],
        "Animals": ["tiger", "lion", "elephant", "zebra", "monkey", "rabbit", "horse", "snake", "panda", "giraffe"],
        "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "black", "white", "brown", "pink"],
        "Countries": ["pakistan", "india", "china", "japan", "brazil", "canada", "france", "italy", "spain", "egypt"]
    }
    
    category_name, words_list = random.choice(list(categories.items()))
    selected_word = random.choice(words_list)
    
    # HINT LABEL
    hint_lbl = Label(root, text=f"HINT: Category is {category_name}", bg="#E7FFFF", fg="black", font=("arial", 25, "bold"))
    hint_lbl.place(x=150, y=70)

    # Dashes
    x = 250
    d_labels = []
    for i in range(len(selected_word)):
        x += 60
        lbl = Label(root, text="_ ", bg="#E7FFFF", fg="black", font=("arial", 40))
        lbl.place(x=x, y=450)
        d_labels.append(lbl)

    # Images dictionaries
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    img_dict = {}
    for let in al:
        try:
            img_dict[let] = PhotoImage(file="{}.gif".format(let))
        except:
            img_dict[let] = None

    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    h_img_dict = {}
    for hangman in h123:
        try:
            img = PhotoImage(file="{}.gif".format(hangman))
            h_img_dict[hangman] = img.subsample(2, 2)
        except:
            h_img_dict[hangman] = None

    button_info = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

    btn_dict = {}
    for q1 in button_info:
        btn_id, letter, x_pos, y_pos = q1
        img = img_dict.get(letter)
        if img:
            btn = Button(root, bd=0, command=lambda l=letter, b=btn_id: check(l, b), bg="#E7FFFF", activebackground="#E7FFFF", font=("arial", 10), image=img)
        else:
            btn = Button(root, text=letter.upper(), bd=1, command=lambda l=letter, b=btn_id: check(l, b), bg="#E7FFFF", fg="black", activebackground="#E7FFFF", font=("arial", 15, "bold"), width=3, height=1)
        btn.place(x=x_pos, y=y_pos)
        btn_dict[btn_id] = btn

    han_info = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    lbl_dict = {}
    for p1 in han_info:
        c_id, h_id = p1
        img = h_img_dict.get(h_id)
        if img:
            lbl = Label(root, bg="#E7FFFF", image=img)
        else:
            lbl = Label(root, text="Mistakes: {} / 6".format(int(h_id[1]) - 1), bg="#E7FFFF", font=("arial", 20, "bold"), fg="red")
        lbl_dict[c_id] = lbl

    if 'c1' in lbl_dict:
        lbl_dict['c1'].place(x=350, y=150)

    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()

    try:
        e1 = PhotoImage(file = 'exit.gif')
        ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font=10,image=e1)
        ex.place(x=770,y=10)
    except:
        ex = Button(root,text="EXIT",bd = 1,command = close,bg="#ff9999",fg="black",activebackground = "#ff9999",font=("arial",15,"bold"))
        ex.place(x=770,y=10)
        
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",fg="black",font = ("arial",25))
    s1.place(x=10,y=10)

    def check(letter, btn_id):
        global count, win_count, run, score
        if btn_id in btn_dict:
            btn_dict[btn_id].destroy()
            
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    d_labels[i].config(text=letter.upper(), fg="black", font=("arial", 40, "underline"))
            
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
            
        else:
            count += 1
            if f'c{count}' in lbl_dict:
                lbl_dict[f'c{count}'].destroy()
            
            c_next = count + 1
            if f'c{c_next}' in lbl_dict:
                lbl_dict[f'c{c_next}'].place(x=350, y=150)
            
            if count == 6:
                answer=messagebox.askyesno('GAME OVER','YOU LOST!\nThe word was: {}\nWANT TO PLAY AGAIN?'.format(selected_word.upper()))
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    root.mainloop()
