# Write your solution here
def column_correct(sudoku: list, column_no: int):
    num_list = []
    for row_index in range(len(sudoku)):
        cell = sudoku[row_index][column_no] 
        if cell > 0 and cell in num_list:
            return False
        else:
            num_list.append(cell)
    return True