# Write your solution here
def create_tuple(x: int, y: int, z: int):
    coords = [x, y, z]
    return (min(coords), max(coords), x + y + z)