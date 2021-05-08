import random
import requests
import string
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import TV

tmdb = TMDb()
tmdb.api_key = '54d503fb88d27a31d51c15e0911a3968'

categories = {
    'Films': [],
    'TV': [],
    'Soccer Teams': ['chelsea', 'real-madrid', 'barcelona', 'manchester-united', 'liverpool', 'arsenal', 'juventus', 'leicester-city', 'tottenham', 'ac-milan', 'wolves', 'atletico-madrid'],
    'Cities': ['moscow', 'san-francisco', 'new-york', 'london', 'dublin', 'rome', 'venice', 'milan', 'new-delhi', 'amritsar', 'mumbai', 'seattle', 'new-jersey', 'philadelphia', 'los-angles']
}

def title_cleaning(title):
    title = title.replace(" ", "-")
    title = title.replace("'", "")
    title = title.replace("I", "i")
    title = title.replace("II", "ii")
    title = title.replace("III", "iii")
    title = title.replace(".", "")
    title = title.replace(":", "")
    title = title.replace("?", "")
    title = title.lower()
    return title


def fetch_movies():
    global categories
    movie = Movie()
    popular = movie.popular()
    top_rated = movie.top_rated()
    now_playing_movies = movie.now_playing()
    popular_title_list = []
    top_rated_title_list = []
    now_playing_movies_list = []

    for p in popular:
        popular_title = p.title
        popular_title = title_cleaning(popular_title)
        popular_title_list.append(popular_title)


    for film in popular_title_list:
        categories["Films"].append(film)

    for t in top_rated:
        top_rated_title = t.title
        top_rated_title = title_cleaning(top_rated_title)
        top_rated_title_list.append(top_rated_title)

    for film in top_rated_title_list:
        categories["Films"].append(film)

    for r in now_playing_movies:
        now_movie_title = r.title
        now_movie_title = title_cleaning(now_movie_title)
        now_playing_movies_list.append(now_movie_title)

    for film in now_playing_movies_list:
        categories["Films"].append(film)

fetch_movies()


def fetch_tv():
    global categories
    tv = TV()
    popular_tv = tv.popular()
    top_rated_tv = tv.top_rated()
    popular_tv_list = []
    top_rated_tv_list = []

    for p in popular_tv:
        pop_tv = p.name
        pop_tv = title_cleaning(pop_tv)
        popular_tv_list.append(pop_tv)

    for tv in popular_tv_list:
        categories['TV'].append(tv)

fetch_tv()


alphabets = string.ascii_letters
user_selection_index = ['Films', 'TV', 'Soccer Teams', 'Cities']
user_index = int(input("Please select the following categories:-"
                       "\n0 for Films"
                       "\n1 for TV Shows"
                       "\n2 for Soccer Teams"
                       "\n3 for Cities"
                       "\nEnter here: "))
user_selection_category = categories[user_selection_index[user_index]]

guess_word = random.choice(user_selection_category)
number_of_lives = 6
mask_word = ""
game_playing = True
def mask_guess_word():
    global mask_word
    global user_guess
    for char in guess_word:
        mask_word = mask_word + "*"
    for i in range(len(guess_word)):
        space_index = []
        if guess_word[i] == "-":
            space_index.append(i)
        for i in range(len(space_index)):
            mask_word = mask_word[:space_index[i]] + "-" + mask_word[space_index[i] + 1:]
mask_guess_word()



def play_game():
    global number_of_lives
    global mask_word
    global game_playing
    global user_selection_index
    difficulty = input("Please select the difficulty level:-"
                       "\n 0 for beginner"
                       "\n 1 for intermediate"
                       "\n 2 for advanced"
                       "\n Enter here: ")
    if difficulty == "0":
        print("You are such a baby!")
        number_of_lives = 12
    elif difficulty == "1":
        print("You like to take on some challenge huh? Let's go!")
        number_of_lives = 6
    elif difficulty == "2":
        print("You are a warrior")
        number_of_lives = 3
    print(f"Selected category: {user_selection_index[user_index]}")
    print(f"Number of lives: {number_of_lives}")
    print(mask_word)
    while game_playing == True:
        user_guess = input("Please enter your guess letter: ")
        if user_guess in alphabets:
                if user_guess in guess_word:
                    indexes = []
                    for i in range(len(guess_word)):
                        if guess_word[i] == user_guess:
                           indexes.append(i)
                           for i in range(len(indexes)):
                               mask_word = mask_word[:indexes[i]] + user_guess + mask_word[indexes[i]+1:]
                    print(mask_word)
                    print(f"Number of lives left: {number_of_lives}")
                    if mask_word == guess_word:
                        print("You guessed it correctly, YOU WON!")
                        break
                elif user_guess not in guess_word:
                    print("Wrong guess")
                    number_of_lives = number_of_lives - 1
                    print(mask_word)
                    print(f"number_of_lives: {number_of_lives}")
                    if number_of_lives < 1:
                        game_playing = False
                        print("You don't have any more lives left")
                        print(f"You lost! The word was: {guess_word}")
        else:
            print("Please enter a valid input")

play_game()


