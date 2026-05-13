# Write your solution here
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
layers = int(input("Layers: "))
square_len = layers * 2 - 1

for row in range(square_len):
    for col in range(square_len):
        cell = min(row, col, square_len - row - 1, square_len - col - 1)
        print(alphabet[layers - cell - 1], end="")
    print()
