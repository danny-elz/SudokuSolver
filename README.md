## Backtracking Algorithm for Sudoku Solver

### Overview

This project utilizes the Backtracking Algorithm to solve Sudoku puzzles. The Backtracking Algorithm is a systematic method for exploring possible solutions to Sudoku grids while ensuring adherence to the Sudoku rules. It efficiently fills each cell, backtracking when necessary, until a solution is found or it's determined that no solution exists.

### Algorithm Explanation

1. **Initialization**: Begin with an empty Sudoku grid, starting with the first cell at the top left corner.

2. **Move to the Next Empty Cell**: Find the next empty cell in the grid. If there are no empty cells left, the puzzle is solved, and the function terminates.

3. **Try Numbers**: For the current empty cell, attempt to fill it with a number from 1 to 9. Start with 1 the number increments until a valid number is found or all numbers have been tried.

4. **Validity Check**: For each number tried, check if it violates Sudoku rules. Sudoku rules dictate that no row, column, or 3x3 subgrid can contain the same number twice. If the current number doesn't violate any rules, proceed to the next empty cell and repeat the process.

5. **Backtracking**: If no valid numbers exist for the current cell (all numbers 1-9 violate the rules), backtrack to the previous cell, undo the previous choice, and try the next number for that cell. This process recurs until a solution is found or it's determined that no solution exists.

6. **Solution Found**: When a valid number is found for the last cell, the algorithm has successfully solved the Sudoku puzzle.

7. **No Solution**: If the algorithm backtracks to the first cell and still cannot find a valid number, it indicates that the initial puzzle is unsolvable. In this case, the algorithm terminates without a solution.

### Demo

![image](https://github.com/danny-elz/SudokuSolver/assets/109995999/656c68a3-46d2-4455-aa79-31decf77b818)



