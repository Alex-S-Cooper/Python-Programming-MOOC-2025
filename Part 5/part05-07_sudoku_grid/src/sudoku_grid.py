# Write your solution here
def row_correct(sudoku: list, row_no: int):
    num_list = []
    for cell in sudoku[row_no]:
        if cell > 0 and cell in num_list:
            return False
        else:
            num_list.append(cell)
    return True

def column_correct(sudoku: list, column_no: int):
    num_list = []
    for row_index in range(len(sudoku)):
        cell = sudoku[row_index][column_no] 
        if cell > 0 and cell in num_list:
            return False
        else:
            num_list.append(cell)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    num_list = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            cell = sudoku[row][column]
            if cell > 0 and cell in num_list:
                return False
            else:
                num_list.append(cell)
    return True

def sudoku_grid_correct(sudoku: list):
    valid_blocks = [0, 3, 6]
    for row in range(len(sudoku)):
        if not row_correct(sudoku, row):
            return False
        for column in range(len(sudoku[row])):
            if not column_correct(sudoku, column):
                return False
            if row in valid_blocks and column in valid_blocks:
                if not block_correct(sudoku, row, column):
                    return False
    return True

if __name__ == "__main__":
    sudoku = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))

