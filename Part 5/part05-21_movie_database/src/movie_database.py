# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    film_data = {}
    film_data["name"] = name
    film_data["director"] = director
    film_data["year"] = year
    film_data["runtime"] = runtime
    database.append(film_data)