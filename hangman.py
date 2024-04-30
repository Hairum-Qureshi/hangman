# aim is to create a hangman game through the terminal
# if the user guesses a letter correctly, they earn points
# if the user guesses an incorrect letter, they lose points
# the user can use points to buy hints
# there are 3 game modes: easy, medium, and hard

import json

with open("./words/easy.json") as json_file:
    easy_words = json.load(json_file)

with open("./words/medium.json") as json_file:
    medium_words = json.load(json_file)

with open("./words/hard.json") as json_file:
    hard_words = json.load(json_file)

game_mode = "easy"

greeting_message = "Hello, welcome to hangman! What game level will you like to play? \n > Easy \n > Medium \n > Hard"
print(greeting_message)

def playGame():
    print("Playing game mode: " + game_mode)

user_input = input("")
if user_input.lower() == "easy":
    playGame()
elif user_input.lower() == "medium":
    game_mode = "medium"
    playGame()
elif user_input.lower() == "hard":
    game_mode = "hard"
    playGame()
else:
    print("command not understood")