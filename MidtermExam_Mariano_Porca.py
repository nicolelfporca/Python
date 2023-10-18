import random

def rollDice():
    return random.randint(1, 6) + random.randint(1, 6)

def firstRoll():
    return rollDice()

def playGame():
    first = firstRoll()
    
    if first == 2:
        print("Sorry, you rolled. Snake Eyes. YOU LOSE!")
    elif first == 3:
        print("Sorry, you rolled. Trey. YOU LOSE!")    
    elif first == 7:
        print("Congratulations, you rolled Seven. YOU WIN!")
    elif first == 11:
        print("Congratulations, you rolled Yo Leven. YOU WIN!")
    elif first == 12:
        print("Sorry, you rolled. Box Cars. YOU LOSE!")

    else:
        print(f"You rolled {first}. Your points {first}. Keep rolling!")

        while True:
            roll = rollDice()
            print(f"You rolled {roll}. Your points {first}. Keep rolling!")
            if roll == first:
                print(f"Congratulations, you rolled {roll}. YOU WIN!")
                break
            elif roll == 7:
                print(f"Sorry, you rolled {roll}. YOU LOSE!")
                break

if __name__ == "__main__":
    while True:
        playAgain = input("\nDo you want to play Craps? (y/n): ").strip().lower()
        if playAgain != "y":
            break
        playGame()
