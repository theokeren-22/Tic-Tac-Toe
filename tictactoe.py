import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe")
        self.window.configure(bg="grey")
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.players = ["X", "O"]
        self.player = random.choice(self.players)
        self.buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.create_ui()

    def create_ui(self):
        self.create_top_frame()
        self.create_bottom_frame()

    def create_top_frame(self):
        top_frame = tk.Frame(
            self.window,
            bg='#5D6D7E',
            width=1000,
            height=250
        )
        top_frame.place(x=0, y=0)

        game_title = tk.Label(
            top_frame,
            bg='#5D6D7E',
            fg='white',
            text='Tic Tac Toe using Python',
            font=('', 48)
        )
        game_title.place(x=135, y=0)

        self.label = tk.Label(top_frame, text=self.player + " Turn", font=('arial', 30), bg="#5D6D7E", fg="white")
        self.label.place(x=440, y=200)

        reset_button = tk.Button(top_frame, text="Restart Game", font=('arial', 30), bg="#5D6D7E", fg="white", command=self.new_game)
        reset_button.place(x=360, y=95)

    def create_bottom_frame(self):
        bottom_frame = tk.Frame(
            self.window,
            bg='#FFFFFF',
            width=400,
            height=400
        )
        bottom_frame.place(x=265, y=300)

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = tk.Button(bottom_frame, text="", font=('consolas', 40), width=5, height=1,
                                                      command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and self.check_winner() is False:
            self.buttons[row][column]['text'] = self.player

            if self.check_winner() is False:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=(self.player + " Turn"))
            elif self.check_winner() is True:
                self.label.config(text=(self.players[0] + " Wins"))
                self.highlight_winner_combination()
                self.disable_buttons()
                messagebox.showinfo("Game Over", f"{self.players[0]} Wins!")
            elif self.check_winner() == "Tie":
                self.label.config(text="Tie!")
                self.disable_buttons()
                messagebox.showinfo("Game Over", "It's a Tie!")

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        elif self.empty_spaces() is False:
            return "Tie"
        else:
            return False

    def empty_spaces(self):
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] == "":
                    return True
        return False

    def new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " Turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")
                self.buttons[row][column].config(state=tk.NORMAL)

    def highlight_winner_combination(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.buttons[row][0].config(bg="green")
                self.buttons[row][1].config(bg="green")
                self.buttons[row][2].config(bg="green")
                return

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column].config(bg="green")
                self.buttons[1][column].config(bg="green")
                self.buttons[2][column].config(bg="green")
                return

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][2].config(bg="green")
            return

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][0].config(bg="green")
            return

    def disable_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(state=tk.DISABLED)

if __name__ == '__main__':
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()
