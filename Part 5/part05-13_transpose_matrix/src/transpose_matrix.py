# Write your solution here
def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix_copy[j][i]