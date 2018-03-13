print ("Hello! To review your subject please answer the following: \n ")

#Lists available for sorting reviews

movies = []
music = []
art = []
literature = []

valid_movie = ["Movie", "movie", "Film", "film"]
valid_music = ["Song", "song", "music", "Music"]
valid_art = ["Art", "art", "Painting", "painting", "Picture"]
valid_literature = ["Literature", "literature", "Book", "book"]

media_type = raw_input("What is the media type?: ")
genre = raw_input("What is the genre?: ")
title = raw_input("What is the title?: ")
year = raw_input("What year was it created?: ")
description = raw_input("Short Description: ")
rating = float(input("Please Rate it from 0.0 - 10.0: "))

review_material = [media_type, genre, title, year, description, rating]

if review_material[0] in valid_movie:
    movies.append(review_material)
elif review_material[0] in valid_music:
    music.append(review_material)
elif review_material[0] in valid_art:
    art.append(review_material)
elif review_material[0] in valid_literature:
    literature.append(review_material)
else:
    print("We are not yet accepting " + review_material[0] + " reviews.")

print("Here are your reviews:\n " + str(movies) + "\n" + str(music) + "\n" + str(art) + "\n" + str(literature))