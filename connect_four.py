import tkinter as tk
from tkinter import messagebox

# Game Constants
ROWS = 6
COLS = 7
SQUARESIZE = 80
WIDTH = COLS * SQUARESIZE
HEIGHT = ROWS * SQUARESIZE


class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four - InternPe")
        self.root.resizable(False, False)

        # Create a 6x7 grid filled with 0s
        self.board = [[0] * COLS for _ in range(ROWS)]
        self.turn = 0  # 0 is for Red, 1 is for Yellow

        # Setup Canvas for the UI
        self.canvas = tk.Canvas(
            root, width=WIDTH, height=HEIGHT, bg="#2980B9")  # Blue board
        self.canvas.pack()

        # Bind mouse click to the drop_piece function
        self.canvas.bind("<Button-1>", self.drop_piece)

        self.draw_empty_board()

    def draw_empty_board(self):
        for c in range(COLS):
            for r in range(ROWS):
                x0 = c * SQUARESIZE + 10
                y0 = r * SQUARESIZE + 10
                x1 = c * SQUARESIZE + SQUARESIZE - 10
                y1 = r * SQUARESIZE + SQUARESIZE - 10
                self.canvas.create_oval(
                    x0, y0, x1, y1, fill="#2C3E50", outline="#2C3E50")  # Dark empty slots

    def drop_piece(self, event):
        # Calculate which column the user clicked
        col = event.x // SQUARESIZE

        if self.is_valid_location(col):
            row = self.get_next_open_row(col)

            # Update the backend matrix
            self.board[row][col] = 1 if self.turn == 0 else 2

            # Update the UI
            self.update_ui(row, col)

            # Check for a win
            if self.winning_move(1 if self.turn == 0 else 2):
                winner = "Red" if self.turn == 0 else "Yellow"
                messagebox.showinfo("Game Over", f"Player {winner} Wins! 🎉")
                self.root.quit()
            elif self.is_tie():
                messagebox.showinfo("Game Over", "It's a Tie! 🤝")
                self.root.quit()

            # Switch turn
            self.turn += 1
            self.turn = self.turn % 2

    def is_valid_location(self, col):
        # If the top row of that column is 0, it's valid
        return self.board[0][col] == 0

    def get_next_open_row(self, col):
        # Start checking from the bottom row going up
        for r in range(ROWS-1, -1, -1):
            if self.board[r][col] == 0:
                return r
        return None

    def update_ui(self, row, col):
        x0 = col * SQUARESIZE + 10
        y0 = row * SQUARESIZE + 10
        x1 = col * SQUARESIZE + SQUARESIZE - 10
        y1 = row * SQUARESIZE + SQUARESIZE - 10

        color = "#E74C3C" if self.turn == 0 else "#F1C40F"  # Red and Yellow pieces
        self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black")

    def winning_move(self, piece):
        # Check horizontal locations
        for c in range(COLS-3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        # Check vertical locations
        for c in range(COLS):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        # Check positively sloped diagonals
        for c in range(COLS-3):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        # Check negatively sloped diagonals
        for c in range(COLS-3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False

    def is_tie(self):
        for c in range(COLS):
            if self.board[0][c] == 0:
                return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
