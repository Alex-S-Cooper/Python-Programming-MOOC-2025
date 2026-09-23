# write your solution here
def create_matrix():
    matrix = []
    with open("matrix.txt") as matrix_file:
        for row in matrix_file:
            new_row = []
            row = row.replace("\n", "")
            for cell in row.split(","):
                new_row.append(int(cell))
            matrix.append(new_row)
    return matrix

def create_matrix_cells():
    matrix = create_matrix()
    matrix_cells = []
    for row in matrix:
        for cell in row:
            matrix_cells.append(cell)
    return matrix_cells

def matrix_sum():
    matrix = create_matrix_cells()
    return sum(matrix)

def matrix_max():
    matrix = create_matrix_cells()
    return max(matrix)

def row_sums():
    row_sums = []
    matrix_rows = create_matrix()
    for row in matrix_rows:
        row_sums.append(sum(row))
    return row_sums




    





