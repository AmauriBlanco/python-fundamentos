filmInception = {
    "Title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

print(filmInception["Title"])

print(filmInception["genre"])

print(filmInception.get("imdbRating"))
print(type(filmInception.get("imdbRating")))

print(filmInception.keys())

print(filmInception.values())

print(filmInception.items())

filmInception["director"] = "Christopher Nolan"

print(filmInception["director"])
print(filmInception.items())


filmInception.update({"imdbRating": 8.7})

print(filmInception.items())

filmInception.pop("director")
print(filmInception.items())
