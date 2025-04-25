###################################################
# achieved -- topic learned -- improved solution for concept study 
# changed solution to class based -- made code modular
###################################################
###################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_5_b_.py
###################################################
###################################################
###################################################

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

import json
import os
import re
from datetime import datetime

filename_of_json = "file_5_b_movies.json"

class MovieRecord:
    _id_counter = 1  # 🔢 Unique ID for each movie

    def __init__(self, title, genre, watch_status=False):
        self.id = MovieRecord._id_counter
        MovieRecord._id_counter += 1

        self.title = title
        self.genre = genre
        self.watch_status = watch_status  # 🎬 False means unwatched, True = watched
        self.added_date = datetime.now()  # 🕰️ Automatically add date when movie is added

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "watch_status": self.watch_status,
            "added_date": self.added_date.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_dict(data):
        return MovieRecord(
            title=data["title"],
            genre=data["genre"],
            watch_status=data["watch_status"] in [True, "True"]
        )

def validate_input(title, genre):
    if not re.match(r"^[A-Za-z\s]+$", title):
        raise ValueError("❌ Invalid title. Only alphabets and spaces are allowed.")
    if not re.match(r"^[A-Za-z\s]+$", genre):
        raise ValueError("❌ Invalid genre. Only alphabets and spaces are allowed.")

def read_all_json():
    if not os.path.exists(filename_of_json):
        return []
    with open(filename_of_json, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # ⚠️ Handle empty or malformed file

def write_all_json(records):
    with open(filename_of_json, 'w') as file:
        json.dump(records, file, indent=4)

def append_movie_record_json(movie):
    validate_input(movie.title, movie.genre)
    records = read_all_json()
    records.append(movie.to_dict())
    write_all_json(records)
    print(f"✅ Added movie '{movie.title}' to watchlist!")

def mark_movie_as_watched(movie_id):
    records = read_all_json()
    for rec in records:
        if rec["id"] == movie_id:
            rec["watch_status"] = True
            print(f"🎉 Marked '{rec['title']}' as watched!")
            break
    write_all_json(records)

def search_movie_by_genre(keyword):
    records = read_all_json()
    result = [rec for rec in records if keyword.lower() in rec["genre"].lower()]
    print(f"🔍 Found {len(result)} movies in genre '{keyword}'")
    return result

def list_unwatched_movies():
    records = read_all_json()
    unwatched = [rec for rec in records if not rec["watch_status"]]
    print(f"🎬 {len(unwatched)} unwatched movies:")
    for rec in unwatched:
        print(f"⏳ {rec['title']} ({rec['genre']})")
    return unwatched

def list_watched_movies():
    records = read_all_json()
    watched = [rec for rec in records if rec["watch_status"]]
    print(f"✅ {len(watched)} watched movies:")
    for rec in watched:
        print(f"🍿 {rec['title']} ({rec['genre']})")
    return watched

# 🧪 Demo usage
if __name__ == "__main__":
    print("\n🎥 Demo run: Movie Watchlist Tracker\n")

    movie_record = MovieRecord(
        title="Django unchained",
        genre="Documentary"
    )
    append_movie_record_json(movie_record)

    movie_record = MovieRecord(
        title="Interstellar",
        genre="Science Fiction"
    )
    append_movie_record_json(movie_record)

    mark_movie_as_watched(movie_id=1)
    search_movie_by_genre("Science")
    list_unwatched_movies()
    list_watched_movies()


###################################################
###################################################
###################################################

# json output
# [
#     {
#         "id": 1,
#         "title": "Django unchained",
#         "genre": "Documentary",
#         "watch_status": true,
#         "added_date": "2025-04-24 15:25:08"
#     },
#     {
#         "id": 2,
#         "title": "Interstellar",
#         "genre": "Science Fiction",
#         "watch_status": false,
#         "added_date": "2025-04-24 15:25:08"
#     }
# ]

###################################################
###################################################
###################################################
    # output
# 🎥 Demo run: Movie Watchlist Tracker

# ✅ Added movie 'Django unchained' to watchlist!
# ✅ Added movie 'Interstellar' to watchlist!
# 🎉 Marked 'Django unchained' as watched!
# 🔍 Found 1 movies in genre 'Science'
# 🎬 1 unwatched movies:
# ⏳ Interstellar (Science Fiction)
# ✅ 1 watched movies:
# 🍿 Django unchained (Documentary)

###################################################
###################################################
###################################################