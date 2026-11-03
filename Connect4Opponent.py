import numpy as np
import Connect4Template as Temp

#Allowing player to pick a slot
def OpponentMove(grid, board, slotIndex):
    #print(f"{Temp.printBoard(board)} \n ---------------")
    print("Which slot you want to put in")
    slot = input("(1-7): ")
    slot = verifyInput(slot, slotIndex)
        
    grid[slotIndex[slot]][slot] = -1
    board[slotIndex[slot]][slot] = 'O'
    slotIndex[slot] = slotIndex[slot] - 1
    return grid, board, slotIndex, slot
    
       
def verifyInput(slot, slotIndex):
    ready = False
    while ready != True:
        if slot.isdigit():
            slot = int(slot) -1

            if 0 <= slot <= 6:
                if slotIndex[slot] == -1:
                    slot = input("It is full already, Please enter again \n(1-7): ")
                else:
                    ready = True
            else: 
                slot = input("slot 1 - 7 only! \n(1-7): ")
        else:
            slot = input("Please Enter a number \n(1-7): ")


    return slot 
    

    
    ##.isdigit()




#OpponentMove(Temp.Grid)
