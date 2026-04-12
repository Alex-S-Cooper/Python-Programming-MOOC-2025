# Write your solution here
def formatted(num_list):
    str_list = []
    for num in num_list:
        str_list.append(f"{num:.2f}")
    return str_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
