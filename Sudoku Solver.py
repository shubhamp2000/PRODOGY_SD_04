def is_valid(board, row, col, num):
    # Check if the number is already present in the row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # Check if the number is already present in the column
    for y in range(9):
        if board[y][col] == num:
            return False
    
    # Check if the number is already present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for x in range(3):
        for y in range(3):
            if board[start_row + x][start_col + y] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Try placing the number
                        
                        if solve_sudoku(board):  # Recursively solve the puzzle
                            return True
                        
                        board[row][col] = 0  # Backtrack if the solution is not valid
                return False  # No valid number found
    return True  # Puzzle solved

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example unsolved Sudoku puzzle (0 represents empty cells)
unsolved_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku Puzzle:")
print_board(unsolved_sudoku)
print("\nSolving...\n")

if solve_sudoku(unsolved_sudoku):
    print("Solved Sudoku Puzzle:")
    print_board(unsolved_sudoku)
else:
    print("No solution exists.")
