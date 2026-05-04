# Write your solution here
def invert(dict):
    new_dict = dict.copy()
    for key in new_dict:
        new_key = dict.pop(key)
        dict[new_key] = key