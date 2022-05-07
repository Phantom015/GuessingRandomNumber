import random
import string
    
def Difficulty(DifficultyInput): #Difficulty options output
    if DifficultyInput == "e":
        print("Difficulty: Easy 1 - 100")
        return random.randint(1, 100) #randint generates a random num between the a, b
    elif DifficultyInput == "m":
        print("Difficulty: Medium 1 - 1000")
        return random.randint(1, 1000)
    elif DifficultyInput == "h":
        print("Difficulty: Hard 1 - 10000")
        return random.randint(1, 10000)

DifficultyLvl = input("\nSelect Difficulty:\n==================\n\nEasy = e\nMedium = m\nHard = h\nHardcore = Any other characters\n:")

while DifficultyLvl != "e" and DifficultyLvl != "m" and DifficultyLvl != "h":
    print(type(DifficultyLvl))
    DifficultyLvl = input("\nSelect Difficulty:\n==================\n\nEasy = e\nMedium = m\nHard = h\nHardcore = Any other characters\n:")

GamesLimit = (input("\nPick a number limit of games you want to play\n:"))

try: #Tries Convverts str from input to int
    int(GamesLimit)
except ValueError: #Repeat question till Valid character written
    while GamesLimit.isdigit() == False:
         GamesLimit = input("Not a Number, try again\n:")

intGamesLimit = int(GamesLimit) #New var for GamesLimit

for i in range(0, intGamesLimit): #Game Limit Loop
    print("\n\n\nGame #" + str(i+1) + " START!\n=============\n")

    hiddenNumber = Difficulty(DifficultyLvl)
    print("Game Limit: ", intGamesLimit, "\n")

    chances = 0
    userGuess = 0

    #print("HiddnNum", hiddenNumber)

    while not userGuess == hiddenNumber and chances<10: #Questions ingame Loop

        try:
            userGuess = int(input("Guess a number\n: "))
            
            if userGuess > hiddenNumber:
                print("Too high!\n")
        
            elif userGuess < hiddenNumber:
                print("Too Low\n")
        
            else:
                print("!!!! That's right !!!!")
        except:
            print("Try Again using a valid number\n")
        chances+=1

    if userGuess != hiddenNumber: #End of Games
        print("### Game Failed ###")
        print("!!!!YOU WON",i,"GAMES!!!!") 
        break
    else:
        print("!!!!YOU WON",i+1,"GAMES!!!!")
