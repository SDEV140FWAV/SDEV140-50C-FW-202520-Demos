from game import Game

def main():
    game = Game()
    finish = False
    while not finish:
        displayGame(game)
        choice = gameMenu(game)
        finish = processChoice(choice, game)
    print(f"Game Over! Final Score {game.calculateScore()}")

def displayGame(game:Game):
    foundation_str = ""
    waste_str = ""
    for i in range(4):
        foundation_str += f"F{i+1}: {str(game.foundations[i]):5s} "
        try:
            card = game.wastes[i].getTopCard()
            game.wastes[i].playCard(card)
        except:
            card = " "
        waste_str += f"W{i+1}: {str(card):6s}"
        
    print(foundation_str)
    print(waste_str)
    if game.card_to_play != None:
        print(f"Drawn Card: {game.card_to_play}")
    else:
        print(f"Remaining Cards({len(game.deck)})")

def gameMenu(game:Game):
    print("Please choose an option: Enter -1 to quit")
    if game.card_to_play != None:
        print("1. Play Drawn Card")
    elif not game.finished():
        print("1. Draw Card")
    else:
        print("1. Finish Game and Calculate Score")
    
    if game.wastePlay():
        print("2. Play Card from Waste Pile")
        print("3. Display Entire Waste Pile")
    try:
        choice = int(input("Your Choice: "))
        if choice == -1:
            return choice
        if (choice < 1) or (choice > 3) or (not game.wastePlay() and choice > 1):
            print("That is an invalid choice")
            return gameMenu(game)
        return choice
    except ValueError:
        print("You entered something that is not a number.")
        return gameMenu(game)
    
def processChoice(choice:int, game:Game):
    if choice == -1:
        return True
    if choice == 1:
        if game.card_to_play != None:
            playCard(game)
            return False
        elif not game.finished():
            game.drawCard()
            return False
        else:
            return True
    if choice == 2:
        playWasteCard(game)
    if choice == 3:
        displayWastePile(game)

def playCard(game:Game):
    pileType = input("Do you want to play on a (F)oundation or (W)aste pile? ")
    if pileType.upper() != 'F' and pileType.upper() != 'W':
        print("Please enter F for foundation and W for waste.")
        return playCard(game)
    if pileType.upper() == 'F':
        pileType = 'foundation'
    else:
        pileType = 'waste'
    prompt = f"Which {pileType} pile (1-4) do you want to play on? "
    pileNum = getPileNumber(prompt) - 1
    try:
        game.playDrawnCard(pileNum, pileType)
    except RuntimeError as e:
        print(e)


def getPileNumber(prompt:str):
    try:
        pileNum = int(input(prompt))
        if pileNum < 1 or pileNum > 4:
            print("Please enter a number 1 - 4")
            return getPileNumber(prompt)
        return pileNum
    except ValueError:
        return getPileNumber(prompt)

def displayWastePile(game:Game):
    pileNum = getPileNumber("Which waste pile do you want to see? ") - 1
    print(game.wastes[pileNum])

def playWasteCard(game:Game):
    wasteNum = getPileNumber("Which waste pile(1-4) do you want to play from? ") - 1
    foundNum = getPileNumber("Which foundation pile (1-4) do you want to play on? ") -1
    try:
        game.playWasteCard(wasteNum,foundNum)
    except RuntimeError as e:
        print(e)


    

if __name__ == "__main__":
    main()