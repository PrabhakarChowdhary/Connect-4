# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:57:20 2021

@author: Deepa
"""
#  Check for horizontal

loop_status = True

for r in range(0,11,2):
    
    for c in range(0,7,2):
        if board[r][c] == board[r][c+2] == board[r][c+4] == board[r][c+6] == "X":
            print("Player wins.")
            loopStatus = False
            break
    if not loopStatus:
        break

#  Check for vertical
    
for c in range(0,13,2):
    
    for r in range(0,5,2):
        if board[r][c] == board[r+2][c] == board[r+4][c] == board[r+6][c] == "X":
            print("Player wins.")
            loopStatus = False
            break
    if not loopStatus:
        break
    
# check for \ diagonal

for c in range(0,13,2):
    
    for r in range(0,11,2):
        
        try:
            
            if board[r][c] == board[r+2][c+2] == board[r+4][c+4] == board[r+6][c+6] == "X":
              loopStatus = False
              break  
            
            print(c,r,"test")
                
        except IndexError:
            print(c,r,"No Test")
            next
            
    if not loopStatus:
        break

# check for / diagonal

for c in range(0,13,2):
    
    for r in range(10,-1,-2):
        
        try:
            
            if board[r][c] == board[r-2][c+2] == board[r-4][c+4] == board[r-6][c+6] == "X":
              loopStatus = False
              break  
            
            print(c,r,"test")
                
        except IndexError:
            print(c,r,"No Test")
            next
            
    if not loopStatus:
        break