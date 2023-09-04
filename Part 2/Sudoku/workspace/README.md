
# Sudoku Solver with GUI

## Objective
Develop a graphical user interface (GUI) for users to play Sudoku. The project serves as a foundational structure to build upon, with functionalities for gameplay and automated solving to be implemented.

## Current Structure

### 1. Setup and Tools
- The project is initiated in Visual Studio Code with Python as the main programming language.
- Tkinter is utilized for creating the graphical user interface, and the unittest library is suggested for future unit testing during development.

### 2. Sudoku Board Design (sudoku_gui.py)
- The `SudokuGUI` class is a skeleton that includes methods to create a window using Tkinter. This will serve as the base for further developments including the Sudoku game and solver implementations.
- The `create_menu` and `create_board` methods are placeholders to implement functionalities for creating a menu and a 9x9 Sudoku board.

### 3. Algorithm Implementation (sudoku_solver.py)
- This file is earmarked to house the backtracking algorithm for solving Sudoku puzzles in future developments.

### 4. Game Logic (sudoku_game.py)
- This file is designated to contain the `SudokuGame` class where the game logic will be implemented in the future. This includes generating new puzzles and checking the validity of moves.

### 5. Unit Testing (test_sudoku.py)
- This file is set to contain unit tests to verify the correct functionality of the different components of the application in future developments.

### 6. Documentation (README.md)
- The README file gives an overview of the project, explaining the objective and tools used, and outlines the steps involved in the development process.

## Next Steps

1. **Implementing the Backtracking Algorithm**:
  - Develop a function to find empty cells and try placing numbers 1 to 9, checking the validity at each step and backtracking if necessary until a solution is found.

2. **Developing the GUI**:
  - Implement the methods to create a Sudoku board grid and a menu with options like reset, check solution, and solve using the backtracking algorithm.

3. **Enhancing User Experience**:
  - Improve the GUI design for a better user experience and implement alerts/messages for incorrect moves or successful completion.

4. **Unit Testing**:
  - Develop unit tests to verify the functionality of the game logic and the backtracking algorithm.

## How to Run
- Open the project in Visual Studio Code.
- Run `main.py` to initialize the application, which will serve as the starting point for future developments.

For further details, refer to the inline comments and documentation within the code files.
