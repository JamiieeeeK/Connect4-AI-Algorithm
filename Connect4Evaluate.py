import numpy as np
import Connect4CheckState as Check



def boardScore(scoreList):
    overall = sum(scoreList)
    return overall
    if any(score > 100000 for score in scoreList):
        return 100000
    elif any(score > 30000 for score in scoreList):
        return 30000 + overall
    else:
        return overall

def evaluate(grid, slotIndex, noList):
    score = [0,0,0,0,0,0,0] #corresponding to the score they get each slot
    if Check.checkEnd(slotIndex):
        return boardScore(score), score

    winSlot = Check.checkSlotToWin(grid, slotIndex)
    for slt in winSlot:
        score[slt] = score[slt] + 10000 # 4 zeros
    threeSlot, twoSlot = Check.checkSlotToThree(grid, slotIndex)
    for slt in threeSlot:
        score[slt] = score[slt] + 1000  # 3 zeros
    for slt in twoSlot:
        score[slt] = score[slt] + 100   # 2 zeros

    for i in range(0, len(noList)):
        if 1 in noList[i] and i not in winSlot:
            score[i] = -4000  # 3 zeros  
   
    #middle slot is better
    for slt in [2,4]:
        score[slt] = score[slt] * 1.10 #is 1.25 good enough heuristic?
    if 1 not in noList[3]:
        score[3] = score[3] * 1.25

    #print(f"winSlot: {winSlot} \nthreeSlot: {threeSlot} \ntwoSlot: {twoSlot}")
    #print(f"score: {score}")
    
    return boardScore(score), score

#Don't waste time on slot that wont help anymore

def calConnected(grid, slot, slotIndex):
    tempGrid = grid
    position = [slotIndex[slot], slot]
    x,y = position
    tempGrid[x][y] = 1

    #Calculate the consecutive positions, sum up to a maximum score
    #collect the location's value in a line, do a sum of consective 4
    #that will be the max value the position can get


#if there are no score that is higher, just pick randomly from 2~4


    
    
