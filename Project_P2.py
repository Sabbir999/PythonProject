import random

def createBoard():
    cards = [i for i in range(1, 9)] * 2
    random.shuffle(cards)
    board = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            board[i][j] = cards.pop()
    
    return board

def playGame():
    gameBoard = createBoard()
    flipped = [[False for _ in range(4)] for _ in range(4)]
    
    while not gameOver(flipped):
        showBoard(gameBoard, flipped)
        try:
            card1 = cardLocation()
            card2 = cardLocation()
        except ValueError:
            print("Invalid input. Please enter valid coordinates.")
            continue
        
        if card1 == card2 or flipped[card1[0]-1][card1[1]-1] or flipped[card2[0]-1][card2[1]-1]:
            print("Invalid selection. Please try again.")
        elif gameBoard[card1[0]-1][card1[1]-1] == gameBoard[card2[0]-1][card2[1]-1]:
            flipped[card1[0]-1][card1[1]-1] = True
            flipped[card2[0]-1][card2[1]-1] = True
            print("Pair match")
        else:
            print("Pair do not match. Select again!")
        
        input("Press Enter to continue...")
    
    print("Congratulations! You have won the game.")

def cardLocation():
    row = int(input("Enter the row (1 to 4): "))  
    col = int(input("Enter the column (1 to 4): "))  
    
    if row < 1 or row > 4 or col < 1 or col > 4:
        raise ValueError("Invalid coordinates.")
    
    return (row, col)

def showBoard(board, flipped):
    for i in range(4):
        for j in range(4):
            if flipped[i][j]:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

def gameOver(flipped):
    for i in range(4):
        for j in range(4):
            if not flipped[i][j]:
                return False
    return True

playGame()
