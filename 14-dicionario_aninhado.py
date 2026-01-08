import pprint
filmsDict = {
    "Inception": {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "Interestellar": {
        "yearRelease": 2014,
        "imdbRating": 8.2,
        "genre": ["Sci-fi", "Drama"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

print(filmsDict["Interestellar"]["yearRelease"])

filmsDict["Inception"]["director"] = "Christopher Nolan"

pp.pprint(filmsDict)

del filmsDict["Interestellar"]

pp.pprint(filmsDict)

