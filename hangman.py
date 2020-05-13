##HANGMAN PROJECT!
import random

def create_progress_str(winning_word, guessed):
    progress_string = "" 
    for letter in winning_word:
        if letter in guessed:
            progress_string = progress_string + letter
        else:
            progress_string = progress_string + '-'
    return progress_string

def check_if_won(winning_word, guessed):
    won = False
    for letter in list(set(winning_word)):
        if letter not in guessed:       
            won = False
            break
        won = True
    return won
def Hangman():
    print("H A N G M A N")
    player = input("type 'play' to play the game or type 'quit' to quit: ")
    if player == "play":
        print("You have 8 tries to guess the word I'm thinking of")
        poss_words = ['python', 'java', 'kotlin', 'javascript','apple','banana','orange','red','yellow','blue','right','left','big',
                      'small','large','kind','mean','nice','good','bad','great','terrible']
        winning_word = poss_words[random.randint(0,len(poss_words)-1)]
        tries = 8
        guessed = []                          
        while tries > 0:
            progress_string = create_progress_str(winning_word, guessed)
            print(progress_string)
            guess = input("please put in a letter or a word: ").lower()
            if len(guess) == 1: #if the guess is a letter
                if guess not in guessed: # if the user hasn't guessed this letter before
                    guessed.append(guess) # add it to the lsit of guessed letters
                    if guess in winning_word: # if the letter is in the word, tell them they guessed correctly
                        print("good guess!")
                        won = check_if_won(winning_word, guessed) #check if they guessed all the letters
                        if won is True: # if they guessed all the letters, they won
                             print("you guessed all the letters in the word!")
                             break
                    else:
                        tries -= 1
                        print("letter not in word. You have %d tries left" %tries)
                        if tries == 0:
                            print("you have lost")
                else:
                    print("You've already guessed this letter. Try again")     
            elif len(guess) > 1:
                if guess == winning_word:
                    print("correct you have won!")
                    break
                else:
                    tries -= 1
                    print("wrong word. You have %d tries left" %tries)
                    if tries == 0:
                        print("you have lost")
        Hangman() 
    elif player == "quit":
        return "ok your loss"
       

