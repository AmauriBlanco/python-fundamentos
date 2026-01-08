moviesList = ["Titanic", "The GodFather", "Inception", "Matrix"]

for movie in moviesList:
    print(movie)
    
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)
    
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)