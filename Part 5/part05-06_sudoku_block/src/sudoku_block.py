# Write your solution here
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