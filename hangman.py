## HANGMAN 
# Author: Sayo Owolabi
# Date: 21/11/2024

import string
import random

def chooseWord():
    """Function to choose a random word from a text file"""
   
    #choose random number
    i = 1
    lineNo = random.randint(1,1000)
    # print(lineNo)
        
    #open word bank for reading
    wordBank = open("hangman-wordlist.txt", "r")
        
    lines = wordBank.readlines()
        
    #get the word that corrolates with the random number
    for line in lines:
        if i == lineNo:
            chosenWord = line
            # print(chosenWord)
                
        i= i+1
        
    wordBank.close()
    
    return chosenWord
    
    
    
def checkmatch(word, currentguess):
    """Function to check if the player has guessed the word"""
    
    #create a string with their correctly guessed letters
    joinedGuessWord = ""
    for char in currentguess:
        joinedGuessWord = joinedGuessWord + char
    
    #determine if they have guessed the word or not
    if joinedGuessWord == word[:-1]:
        print("\nThe word was", word)
        return True
    else:
        return False
    
   
    
def mainGame(word):
    """The main body of the game""" 
    
       
    gamestate = [None] * 8
    gamestate = [
        "\n\n7 chances left",
        "\n\n6 chances left",
        "\n\n5 chances left",
        "\n\n4 chances left",
        "\n\n3 chances left",
        "\n\n2 chances left",
        "\n\n1 chance left",  
        "\n\nGame Over"
    ]

    lifeCounter = 0
    playerWord = ''
    i = 0
    playerGuess = ''
    incorrectguesses = ['']

    
    #get blank string the same length as the word
    
    playerWord = [None] * (len(word)-1)
    for i in range(0,len(playerWord)):
        playerWord[i] = "_"
    
    while lifeCounter != 8:
        j = 0
        correct = False
        
        #print their current progress
        print("\n\n" , playerWord,"\n\n") 
        
        #prompt for a guess
        playerGuess = input("\n\nGuess a letter: \n")
    
        #check if the guessed letter is in the word
        for char in word:
            if char == playerGuess:
                print("\n\nCORRECT\n\n")
                print("---------------------------------------------------------------")
                
                #place the letter in the correct space
                playerWord[j] = char
                
                correct = True
                
            j = j+ 1
                
        if correct == False:
            
            #Add the wrong guess to the incorrect guess list
            incorrectguesses.append(playerGuess)
            
            
            print("\n\nNot in word\nIncorrect Guesses:", incorrectguesses[1:], "\n")
            print("---------------------------------------------------------------")
            
            #Update the amount of chances left
            print(gamestate[lifeCounter])
            lifeCounter = lifeCounter + 1
        
        #check if they have guessed the word
        check = checkmatch(word, playerWord) 
        
        if check == True:
            print("You win!")
            print("---------------------------------------------------------------")
            return 1
        
    #reveal the word if they lost and return to the menu    
    print("\nThe word was", word)
    print("---------------------------------------------------------------")
    return 2
                
            


def menu():
    """Menu Function"""
    choice = 2

    print("\n\nGuess the word in 8 tries!\n")


    while choice != 0:
        choice = int(input("1 to play\n0 to end: "))
        print("---------------------------------------------------------------")
        
        
        if choice == 1:
            word = chooseWord()
            winorlose = mainGame(word)
            
        #if they won the last game, end the program
        if winorlose == 1:
            choice = 0
            
        #if they lost the last game give the option to try again
        elif winorlose == 2:
            print("\nTry again?\n")
          

#start game
menu()
        
    