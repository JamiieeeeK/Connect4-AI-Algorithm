import numpy as np
import random
import copy
import Connect4Template as Temp
import Connect4Opponent as Opp
import Connect4Evaluate as Eval
import Connect4CheckState as Check
import Connect4AlphaBeta as AB

InitialGrid = Temp.Grid  #6x7
InitialBoard = Temp.board
InitialSlotIndex = [5, 5, 5, 5, 5, 5, 5]



currentPlayer = random.choice([-1,1]) #player is -1, code is 1

def main():
    End = False
    while End != True:
        runGame()
        contu = input("nextGame? (Y/N): ").upper()
        contu = verifyInput(contu)
        if contu == "N":
            End = True
        else:
            print("\nLet's Start Again!")
    print ("Thank you for playing")

    


    
def runGame():
    global currentPlayer
    Grid = copy.deepcopy(InitialGrid)
    Board = copy.deepcopy(InitialBoard)
    SlotIndex = copy.deepcopy(InitialSlotIndex)
    NoList = [[12], [12], [12], [12], [12], [12], [12]]
    print(f"Hi, Welcome to Connect 4, You are O and I am X. Enjoy!\n{Temp.printBoard(Board)} \n ---------------")
    PlayerWin = False
    CodeWin = False

    if currentPlayer == 1:
        Slot = FirstMove()
        NoList = IncNoList(NoList,Slot)
        Grid, Board, SlotIndex = updateGrid(Grid, Board, SlotIndex, Slot)
        print("I'll start first: ")
        print(f"{Temp.printBoard(Board)} \n ---------------")
        currentPlayer = -1

    while Check.checkEnd(SlotIndex) == False:
        if currentPlayer == -1:
            Grid, Board, SlotIndex, Slot = Opp.OpponentMove(Grid, Board, SlotIndex)
            print(Temp.printBoard(Board))
            print(" --------------- ")
            PlayerWin = Check.checkWin(Grid, Slot, currentPlayer, SlotIndex) #-1

        if currentPlayer == 1:
            Slot, NoList = FindBestSlot(Grid, Slot, SlotIndex, NoList)
            Grid, Board, SlotIndex = updateGrid(Grid, Board, SlotIndex, Slot)
            print("my turn:")
            print(f"{Temp.printBoard(Board)} \n ---------------")
            CodeWin = Check.checkWin(Grid, Slot, currentPlayer, SlotIndex) #1
        NoList = IncNoList(NoList,Slot)


        if PlayerWin == True:
            print("Well Done, you beat me")
            break
        if CodeWin == True:
            print("Sorry, get better luck next time")
            break
        
        currentPlayer = currentPlayer*-1
        #print(SlotIndex)
        #print(Check.checkEnd(SlotIndex))
        
    if Check.checkEnd(SlotIndex) == True and PlayerWin == False and CodeWin == False:
        print("Wow, this is a draw")
        
            
        

def updateGrid(grid, board, slotIndex, slot):
    grid[slotIndex[slot]][slot] = 1
    board[slotIndex[slot]][slot] = 'X'
    slotIndex[slot] = slotIndex[slot] - 1
    return grid, board, slotIndex

def IncNoList(noList, slot):
    noList[slot] = [val - 1 for val in noList[slot]]
    return noList

def FirstMove():
    slot = random.choice([0,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6])
    return slot
    
    
def FindBestSlot(grid, opSlot, slotIndex, noList):
    winSlot = Check.checkSlotToWin(grid, slotIndex)
    if not winSlot:
        blockList, noList = Check.checkThree(grid, opSlot, slotIndex, noList)
        if blockList != [] and blockList != None:
            slot = random.choice(blockList)
            noList[slot].remove(0)
            print(f"noList after block: {noList}")
        else:
            score, slot = AB.AlphaBeta(grid, 0, -float('inf'), float('inf'), 1, slotIndex, noList, None)
            print(score)
            print(noList)

    else:
        slot = random.choice(winSlot)

    
    #adapt Eval    
    return slot, noList

def verifyInput(contu):
    while contu.upper() not in ["Y", "N"]:
        contu = input("Invalid Input - Please Enter Again \nnextGame? (Y/N): ").upper()
    return contu


main()

#print(InitialGrid)
