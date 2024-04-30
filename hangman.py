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

greeting_message = "Hello, welcome to hangman! What game level will you like to play? \n > Easy \n > Medium \n > Hard"
print(greeting_message)