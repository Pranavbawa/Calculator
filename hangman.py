import random
categories = {
    'Films': ['shawshank-redemption', 'inception', 'batman-begins', 'saving-private-ryan', 'andhadhun', 'shutter-island', 'get-out', 'girl-next-door', 'man-of-steel', 'justice-league', 'forrest-gump'],
    'Soccer Teams': ['chelsea', 'real-madrid', 'barcelona', 'manchester-united', 'liverpool', 'arsenal', 'juventus', 'leicester-city', 'tottenham', 'ac-milan', 'wolves', 'atletico-madrid'],
    'Cities': ['moscow', 'san-francisco', 'new-york', 'london', 'dublin', 'rome', 'venice', 'milan', 'new-delhi', 'amritsar', 'mumbai', 'seattle', 'new-jersey', 'philadelphia', 'los-angles']
}
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
user_selection_index = ['Films', 'Soccer Teams', 'Cities']
user_index = int(input("Please select the following categories:-"
                       "\n0 for Films"
                       "\n1 for Soccer Teams"
                       "\n2 for Cities"
                       "\nEnter here: "))
user_selection_category = categories[user_selection_index[user_index]]

guess_word = random.choice(user_selection_category)
number_of_lives = 5
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
    print(f"Select category: {user_selection_index[user_index]}")
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


