# Write your solution here
def find_movies(database: list, search_term: str):
    found = []
    for film in database:
        if search_term in film["name"].lower():
            found.append(film)
    return found
