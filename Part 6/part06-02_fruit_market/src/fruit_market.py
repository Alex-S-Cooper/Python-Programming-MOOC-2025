# write your solution here
def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as fruits_file:
        for line in fruits_file:
            line = line.replace("\n", "")
            cells = line.split(";")
            fruits_dict[cells[0]] = float(cells[1])
    return fruits_dict 


