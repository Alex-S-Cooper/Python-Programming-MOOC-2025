# Write your solution here
def print_sudoku(sudoku: list):
    for r in range(len(sudoku)):
        for c in range(len(sudoku[r])):
            cell = ""
            if sudoku[r][c] == 0:
                cell = "_"
            else:
                cell = sudoku[r][c]

            if c == len(sudoku[r]) - 1:
                print(cell, end="")
            else:
                print(f'{cell} ', end="")
            
            if c == 2 or c == 5:
                print(" ", end="")
        if r == 2 or r == 5:
            print()
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    s = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(s)