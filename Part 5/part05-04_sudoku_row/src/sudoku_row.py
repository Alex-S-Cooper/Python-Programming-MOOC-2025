# Write your solution here
def row_correct(sudoku: list, row_no: int):
    num_list = []
    for cell in sudoku[row_no]:
        if cell > 0 and cell in num_list:
            return False
        else:
            num_list.append(cell)
    return True
        