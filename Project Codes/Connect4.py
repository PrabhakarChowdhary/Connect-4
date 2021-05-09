# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:25:59 2021

@author: PC

Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. 
In this project, your task is create a Connect 4 game in Python. 
Before you get started, please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward. 
You'll want to draw the board, and allow two players to take turns placing their pieces 
on the board (but as you learned above, they can only do so by choosing a column, not a row). 
The first player to get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.


Extra Credit:

Want to try colorful pieces instead of X and O? 
First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, but try and see if you can figure it out 
on your own. Or you might be able to find unicode characters to use instead, 
depending on what your system supports. Here's a hint: print(u'\u2B24')

"""

# Draw the initial board ( Connect 4 has a 6 rows and 7 column matrix)

board = []

# initiate board


def initBoard():
    
    for r in range(11):
        
        row = []
        
        for c in range(13):
            
            if (r+1)%2 == 0:
                row.append("-")
            else:
                if (c+1)%2 == 0:
                    row.append("|")
                else:
                    row.append(" ")
                    
        board.append(row)
        
    return(board)

# draw board
    
def drawBoard():
    
    for r in range(11):
        
        for c in range(13):
    
            if (c+1)%13 == 0:
                print(board[r][c])
            else:
                print(board[r][c], end=(""))
                
# # Function to check who won the game

def checkWin(board,playerMark):
    #  Check for horizontal

    loopStatus = True
    
    for r in range(0,11,2):
        
        for c in range(0,7,2):
            if board[r][c] == board[r][c+2] == board[r][c+4] == board[r][c+6] == playerMark:

                loopStatus = False
                break
        if not loopStatus:
            break
    
    #  Check for vertical
        
    for c in range(0,13,2):
        
        for r in range(0,5,2):
            if board[r][c] == board[r+2][c] == board[r+4][c] == board[r+6][c] == playerMark:

                loopStatus = False
                break
        if not loopStatus:
            break
        
    # check for \ diagonal
    
    for c in range(0,13,2):
        
        for r in range(0,11,2):
            
            try:
                
                if board[r][c] == board[r+2][c+2] == board[r+4][c+4] == board[r+6][c+6] == playerMark:
                  loopStatus = False
                  break  
                

                    
            except IndexError:

                next
                
        if not loopStatus:
            break
    
    # check for / diagonal
    
    for c in range(0,13,2):
        
        for r in range(10,-1,-2):
            
            try:
                
                if board[r][c] == board[r-2][c+2] == board[r-4][c+4] == board[r-6][c+6] == playerMark:
                  loopStatus = False
                  break  
              
                  
            except IndexError:
                next
                
        if not loopStatus:
            break
    
    return(loopStatus)


# Initial board conditions

board = initBoard()
player = 1

# Game Loop

while 1:
    
    print("Player 1 ",u"\u25CF")
    print("Player 2 ",u"\u25CB")
    
    drawBoard()

    # Seek valid inpt loop

    while 1:
        
        if player == 1:
            move = int(input("Player 1: Please enter the column (1 to 7) to play:\n"))
        else:
            move = int(input("Player 2: Please enter the column (1 to 7) to play:\n"))
            
        if move > 7 or move < 1:
            print("Please enter a value between 1 and 7")
            continue
            
        tempcol = ((move*2)-1)
        col = tempcol - 1
            
        if board[0][col] == " ":
            break
        else:
            print("The column is full. PLease choose another column.\n")
    
    # Simulate gravity for move    
                
    for r in range(11):
        if board[10][col] == " ":
            row = 10
        else:
            if r%2 != 0:
                continue
            else:                
                if board[r][col] == " ":
                    continue
                else:
                    row = r-2
                    break
                    
    # Execute the move into the game state list
    
    if player == 1:
        board[row][col] = u'\u25CF'
        playerMark = u'\u25CF'
    else:
        board[row][col] = u'\u25CB'
        playerMark = u'\u25CB'
        
    winStatus = checkWin(board,playerMark)
    
    if not winStatus:
        drawBoard()
        print("\nPlayer ",player," wins. ",playerMark)
        break
                        
    # Place for checking if last player won
    
    # Change the player turn
    
    if player == 1:
        player = 2
    else:
        player = 1
                

            
        
