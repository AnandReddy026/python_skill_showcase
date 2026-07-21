import tkinter as tk
from tkinter import messagebox

# Main window setup
root = tk.Tk()
root.title("Tic Tac Toe - InternPe")
root.configure(bg="#2C3E50")

# Variables to track turns and move counts
clicked = True
count = 0

# Function to disable all buttons after a win or tie


def disable_all_buttons():
    for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        b.config(state="disabled")

# Function to check if someone won


def check_win():
    global count
    win = False

    # All possible winning combinations
    win_conditions = [
        (b1, b2, b3), (b4, b5, b6), (b7, b8, b9),  # Horizontal
        (b1, b4, b7), (b2, b5, b8), (b3, b6, b9),  # Vertical
        (b1, b5, b9), (b3, b5, b7)                # Diagonal
    ]

    for condition in win_conditions:
        if condition[0]["text"] == condition[1]["text"] == condition[2]["text"] != " ":
            # Highlight winning line
            condition[0].config(bg="#27AE60", fg="white")
            condition[1].config(bg="#27AE60", fg="white")
            condition[2].config(bg="#27AE60", fg="white")
            win = True
            messagebox.showinfo(
                "Game Over", f"Player {condition[0]['text']} Wins! 🎉")
            disable_all_buttons()
            return

    # Check for tie
    if count == 9 and not win:
        messagebox.showinfo("Game Over", "It's a Tie! 🤝")
        disable_all_buttons()

# Function triggered when a button is clicked


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        b.config(fg="#E74C3C")  # Red color for X
        clicked = False
        count += 1
        check_win()
    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        b.config(fg="#3498DB")  # Blue color for O
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror(
            "Error", "Hey! That box is already selected. Pick another one.")


# Creating the grid buttons
font_style = ("Helvetica", 24, "bold")
bg_color = "#ECF0F1"

b1 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b1))
b2 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b2))
b3 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b3))

b4 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b4))
b5 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b5))
b6 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b6))

b7 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b7))
b8 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b8))
b9 = tk.Button(root, text=" ", font=font_style, height=3,
               width=6, bg=bg_color, command=lambda: b_click(b9))

# Placing buttons on the screen using grid layout
b1.grid(row=0, column=0, padx=2, pady=2)
b2.grid(row=0, column=1, padx=2, pady=2)
b3.grid(row=0, column=2, padx=2, pady=2)

b4.grid(row=1, column=0, padx=2, pady=2)
b5.grid(row=1, column=1, padx=2, pady=2)
b6.grid(row=1, column=2, padx=2, pady=2)

b7.grid(row=2, column=0, padx=2, pady=2)
b8.grid(row=2, column=1, padx=2, pady=2)
b9.grid(row=2, column=2, padx=2, pady=2)

# Start the application
root.mainloop()
