
import tkinter as tk
from tkinter import messagebox
from sudoku_game import SudokuGame
from sudoku_solver import SudokuSolver

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.game = SudokuGame()
        self.solver = SudokuSolver()
        self.board = self.game.generate_puzzle('easy')
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_menu()
        self.create_board()
                #self.window.mainloop()  # Moved this line to a separate method

    def mainloop(self):
        self.window.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        difficulty_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Difficulty", menu=difficulty_menu)
        difficulty_menu.add_command(label="Easy", command=lambda: self.start_new_game('easy'))
        difficulty_menu.add_command(label="Medium", command=lambda: self.start_new_game('medium'))
        difficulty_menu.add_command(label="Hard", command=lambda: self.start_new_game('hard'))

    def create_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(self.window, width=3, font=('Arial', 24), justify='center')
                self.cells[row][col].grid(row=row, column=col)
                self.cells[row][col].insert(0, str(self.board[row][col]) if self.board[row][col] != 0 else '')
                self.cells[row][col].bind("<KeyRelease>", self.validate_input)
        
        check_solution_button = tk.Button(self.window, text="Check Solution", command=self.check_solution)
        check_solution_button.grid(row=9, column=0, columnspan=9)

    def validate_input(self, event):
        try:
            value = int(event.widget.get())
            if value < 1 or value > 9:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 9.")
            event.widget.delete(0, tk.END)

    def start_new_game(self, difficulty):
        self.board = self.game.generate_puzzle(difficulty)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board[row][col]) if self.board[row][col] != 0 else '')

    def check_solution(self):
        user_solution = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].get() != '':
                    user_solution[row][col] = int(self.cells[row][col].get())
        
        if self.solver.validate(user_solution):
            messagebox.showinfo("Congratulations", "Your solution is correct!")
        else:
            messagebox.showwarning("Incorrect Solution", "Your solution is incorrect. Please try again.")
