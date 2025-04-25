################################################
# planned topic .json file handling
################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_5_a_.py
################################################
# improved clean code (modular) in 

# # Assignment - 5
# Movie Watchlist Tracker

# Features:

#   (a)     Add a movie (title, genre, watch status)

#   (b)     Mark as watched

#   (c)     Search by genre

#   (d)     List all unwatched movies
            # list all watched movies

#   (e)     Store in .json



########################################
# [
#     {
#         "title": "jumanji",
#         "genre": "children",
#         "watched": false
#     },
    
#     {
#         "title": "kungfu",
#         "genre": "teen",
#         "watched": false
#     },
#     {
#         "title": "jumanji",
#         "genre": "children",
#         "watched": false
#     },
    
#     {
#         "title": "vampire",
#         "genre": "youth",
#         "watched": true
#     }

# ]
########################################


import json

json_filename = 'file_5.json'

###########################################################
###########################################################


# Function to load movies from the JSON file
def load_movies ():
    try:
        with open(json_filename, 'r') as json_file:
            print("loading movies ...")
            movies = json.load(json_file)
            print(movies)
            return movies

    except Exception as e:

        if e == FileNotFoundError:
            print("file not found. starting with  an empty movies list") # sn=

        print(f"❌ Error loading movies: {e}")

        return []

###########################################################
###########################################################

    # mark as watched
    # movies = mark_movie_watched(True, movies)


def mark_movie_watched(title, movies):
    for movie in movies:
        if movie["title"] == title:
            print(movie)
            movie["watched"] = True
            print(movie)
        
        print(f"Movie marked as watched: {title}")
        return movies
    
    print(f"No movie found with the tile {title}")
    return movies

###########################################################
###########################################################

    #   (a)     Add a movie (title, genre, watch status)
    # movies = add_movie("spider", "adult")

def add_movie(title, genre ):
    movie = {
        
    }
###########################################################
###########################################################

# Save the updated movie list
    # save_movies(movies)

### Function to save movies to the JSON file
def save_movies(movies):
    try:
        with open(json_filename, 'w') as json_file:
            json.dump(movies, json_file, indent= 4)
            print(" ✅ writing movie list to JSON file done  ...")

    except Exception as e:

        if e == FileNotFoundError:
            print("file not found. starting with  an empty movies list") # sn=

        print(f"❌ Error loading movies: {e}")

        return []

###########################################################
###########################################################

def main():

    print("======================================")
    
    movies = load_movies()

    print("======================================")

    #   (b)     Mark as watched
    movies = mark_movie_watched("jumanji", movies)

    print("======================================")
    print("======================================")

    #   (a)     Add a movie (title, genre, watch status)

    movies = add_movie("spider", "adult")



    print("======================================")

    # Save the updated movie list
    save_movies(movies)

    print("======================================")
    print("======================================")


if __name__ == '__main__':
    main()


