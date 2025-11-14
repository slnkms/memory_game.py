# This is a Memory Game.

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import random
import os

window = tk.Tk()
window.title("Memory Game")
window.geometry("600x600+700+300")
window.minsize(600, 600)
window.maxsize(600, 600)
window["bg"] = "#BA8BB0"

# Variables

flipped = []
buttons = []
cards = []
back_image = None

victory_label = None
btn_again = None
btn_back_to_menu = None
again_handler = None

is_comparing = None


# Functions

def start_game():
    button_start.pack_forget()
    button_exit.pack_forget()
    title.config(
        text="Choose Your Theme",
        font=("Arial", 30, "bold"),
        bg="#BA8BB0",
        fg="#BD1699"
    )

    tk.Label(window, bg="#BA8BB0").pack(expand=True)

    button_jelly.pack(pady=15)
    button_cat.pack(pady=15)
    button_food.pack(pady=15)
    button_bunny.pack(pady=15)
    button_back.pack(pady=40)

    tk.Label(window, bg="#BA8BB0").pack(expand=True)

def exit_game():
    window.destroy()

def back_to_menu():
    button_jelly.pack_forget()
    button_cat.pack_forget()
    button_food.pack_forget()
    button_bunny.pack_forget()
    button_back.pack_forget()

    title.config(text="Memory Game")
    button_start.pack(pady=20)
    button_exit.pack(pady=20)

def select_jelly():
    button_jelly.pack_forget()
    button_cat.pack_forget()
    button_back.pack_forget()
    title.pack_forget()

    title.config(text="Jelly Memory", fg="white")

    show_jelly()

def show_jelly():
    global cards, buttons, back_image, flipped, again_handler
    clear_game_area()

    for widget in window.winfo_children():
        try:
            widget.pack_forget()
        except:
            pass

    again_handler = play_again_jelly

    base_dir = os.path.dirname(__file__)

    images = []
    for i in range(1, 9):
        img_path = os.path.join(base_dir, f"jelly{i}.png")
        img = Image.open(img_path)
        img = img.resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

    cards = images * 2
    random.shuffle(cards)

    back_path = os.path.join(base_dir, "back.png")
    back_image =ImageTk.PhotoImage(Image.open(back_path).resize((80, 80)))

    buttons = []
    flipped = []

    for row in range(4):
        for col in range(4):
            index = row * 4 + col
            btn = tk.Button(
                window,
                image=back_image,
                command=lambda i=index: flip_card(i),
                bd=0,
                bg="#BA8BB0",
                activebackground="#BA8BB0"
            )
            btn.place(x=100 + col * 100, y=100 + row * 100)
            buttons.append(btn)

def select_food():
    try: button_jelly.pack_forget()
    except: pass
    try: button_cat.pack_forget()
    except: pass
    try: button_food.pack_forget()
    except: pass
    try: button_bunny.pack_forget()
    except: pass

    title.pack_forget()
    title.config(text="Food Memory", fg="white")
    show_food()

def show_food():
    global cards, buttons, back_image, flipped, again_handler

    clear_game_area()

    for widget in window.winfo_children():
        try:
            widget.pack_forget()
        except:
            pass

    base_dir = os.path.dirname(__file__)

    images = []
    for i in range(1, 9):
        img_path = os.path.join(base_dir, f"food{i}.png")
        img = Image.open(img_path).resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

    cards = images * 2
    random.shuffle(cards)

    back_path = os.path.join(base_dir, "back.png")
    back_image = ImageTk.PhotoImage(Image.open(back_path).resize((80, 80)))

    buttons = []
    flipped = []

    again_handler = play_again_food

    for row in range (4):
        for col in range(4):
            index = row * 4 + col
            btn = tk.Button(
                window,
                image=back_image,
                command=lambda i=index: flip_card(i),
                bd=0,
                bg="#BA8BB0",
                activebackground="#BA8BB0"
            )
            btn.place(x=100 + col * 100, y=100 + row * 100)
            buttons.append(btn)

def play_again_food():
    clear_game_area()
    show_food()

def select_bunny():
    try: button_jelly.pack_forget()
    except: pass
    try: button_cat.pack_forget()
    except: pass
    try: button_food.pack_forget()
    except: pass
    try: button_bunny.pack_forget()
    except: pass
    try: button_back.pack_forget()
    except: pass

    title.pack_forget()
    title.config(text="Bunny Memory", fg="white")
    show_bunny()

def show_bunny():
    global cards, buttons, back_image, flipped, again_handler

    clear_game_area()

    for widget in window.winfo_children():
        try:
            widget.pack_forget()
        except:
            pass

    base_dir = os.path.dirname(__file__)

    images = []
    for i in range(1, 9):
        img_path = os.path.join(base_dir, f"bunny{i}.png")
        img = Image.open(img_path).resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

    cards = images * 2
    random.shuffle(cards)

    back_path = os.path.join(base_dir, "back.png")
    back_image = ImageTk.PhotoImage(Image.open(back_path).resize((80, 80)))

    buttons = []
    flipped = []

    again_handler = play_again_bunny

    for row in range(4):
        for col in range(4):
            index = row * 4 + col
            btn = tk.Button(
                window,
                image=back_image,
                command=lambda i=index: flip_card(i),
                bd=0,
                bg="#BA8BB0",
                activebackground="#BA8BB0"
            )
            btn.place(x=100 + col * 100, y=100 + row * 100)
            buttons.append(btn)

def play_again_bunny():
    clear_game_area()
    show_bunny()


def flip_card(index):
    global flipped, is_comparing

    if is_comparing:
        return

    if buttons[index]["state"] == "disabled":
        return
    
    buttons[index].config(image=cards[index], state="disabled")
    flipped.append(index)

    if len(flipped) == 2:
        is_comparing = True
        window.after(600, check_match)
    elif len(flipped) > 2:
        return

def check_match():
    global flipped, is_comparing

    if len(flipped) < 2:
        is_comparing = False
        flipped = []
        return

    first, second = flipped[:2]

    if cards[first] == cards[second]:
        buttons[first].config(state="disabled")
        buttons[second].config(state="disabled")
    else:
        buttons[first].config(image=back_image, state="normal")
        buttons[second].config(image=back_image, state="normal")

    flipped = []
    is_comparing = False

    if all(btn["state"] == "disabled" for btn in buttons):
        show_victory_ui()

def clear_game_area():
    global buttons, victory_label, btn_again, btn_back_to_menu
    for b in buttons:
        try:
            b.destroy()
        except:
            pass
    buttons = []

    if victory_label:
        try: victory_label.destroy()
        except: pass
        victory_label = None
    if btn_again:
        try: btn_again.destroy()
        except: pass
        btn_again = None
    if btn_back_to_menu:
        try: btn_back_to_menu.destroy()
        except: pass
        btn_back_to_menu = None

def show_victory_ui():
    global victory_label, btn_again, btn_back_to_menu, again_handler

    messagebox.showinfo("Victory!", "Congratulations! All cards are matched!")

    victory_label = tk.Label(
        window,
        text="Congratulations! You found them all!",
        font=("Arial", 16, "bold"),
        bg="#BA8BB0",
        fg="#BD1699"
    )
    victory_label.place(x=300, y=500, anchor="center")

    btn_again = tk.Button(
        window,
        text="Play Again",
        font=("Arial", 16, "bold"),
        bg="#BA8BB0",
        fg="#BD1699",
        width=12,
        command=(again_handler if again_handler else lambda: None)
    )
    btn_again.place(x=170, y=540)

    btn_back_to_menu = tk.Button(
        window,
        text="Back to Menu",
        font=("Arial", 16, "bold"),
        bg="#BA8BB0",
        fg="#BD1699",
        width=12,
        command=return_to_theme_selection
    )
    btn_back_to_menu.place(x=330, y=540)

def play_again_jelly():
    clear_game_area()
    show_jelly()

def return_to_theme_selection():
    clear_game_area()
    title.config(text="Choose Your Theme", fg="#BD1699", bg="#BA8BB0")
    if not title.winfo_ismapped():
        title.pack(pady=20)
    button_jelly.pack(pady=15)
    button_cat.pack(pady=15)
    button_food.pack(pady=15)
    button_bunny.pack(pady=15)
    button_back.pack(pady=40)


def select_cat():
    button_jelly.pack_forget()
    button_cat.pack_forget()
    button_back.pack_forget()
    title.pack_forget()

    title.config(text="Cat Memory", fg="white")

    show_cat()

def show_cat():
    global cards, buttons, back_image, flipped, again_handler

    clear_game_area()

    for widget in window.winfo_children():
        try:
            widget.pack_forget()
        except:
            pass

    base_dir = os.path.dirname(__file__)

    images = []
    for i in range(1, 9):
        img_path = os.path.join(base_dir, f"cat{i}.png")
        img = Image.open(img_path).resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

    cards = images * 2
    random.shuffle(cards)

    back_path = os.path.join(base_dir, "back.png")
    back_image = ImageTk.PhotoImage(Image.open(back_path).resize((80, 80)))

    buttons = []
    flipped = []

    again_handler = play_again_cat

    for row in range(4):
        for col in range(4):
            index = row * 4 + col
            btn = tk.Button(
                window,
                image=back_image,
                command=lambda i=index: flip_card(i),
                bd=0,
                bg="#BA8BB0",
                activebackground="#BA8BB0"
            )
            btn.place(x=100 + col * 100, y=100 + row * 100)
            buttons.append(btn)

def play_again_cat():
    clear_game_area()
    show_cat()


# Title

title = tk.Label(
    window, 
    text="Memory Game", 
    font=("Arial", 30, "bold"), 
    bg="#BA8BB0",
    fg="#BD1699"
)
title.pack(pady=20)

# Buttons

button_start = tk.Button(
    window,
    text="Start",
    font=("Arial", 20, "bold"),
    width=15,
    bg="#BA8BB0",
    fg="#BD1699",
    activebackground="#BA8BB0",
    command=start_game
)
button_start.pack(pady=15)

button_exit = tk.Button(
    window,
    text="Exit",
    font=("Arial", 20, "bold"),
    width=15,
    bg="#BA8BB0",
    fg="#BD1699",
    activebackground="#F7C5CC",
    command=exit_game
)
button_exit.pack(pady=15)

button_jelly = tk.Button(
    window,
    text="Jelly",
    font=("Arial", 20, "bold"),
    bg="#BA8BB0",
    fg="#BD1699",
    width=15,
    command=select_jelly
)

button_cat = tk.Button(
    window,
    text="Cat",
    font=("Arial", 20, "bold"),
    bg="#BA8BB0",
    fg="#BD1699",
    width=15,
    command=select_cat
)

button_food = tk.Button(
    window,
    text="Food",
    font=("Arial", 20, "bold"),
    bg="#BA8BB0",
    fg="#BD1699",
    width=15,
    command=select_food
)

button_bunny = tk.Button(
    window,
    text="Bunny",
    font=("Arial", 20, "bold"),
    bg="#BA8BB0",
    fg="#BD1699",
    width=15,
    command=select_bunny
)

button_back = tk.Button(
    window,
    text="Back",
    font=("Arial", 20, "bold"),
    bg="#BA8BB0",
    fg="#BD1699",
    width=10,
    command=back_to_menu
)

tk.Label(window, bg="#BA8BB0").pack(expand=True)

window.mainloop()