import numpy as np
import random
import Connect4Template


def collect(grid, slot, slotIndex):
    r, c = slotIndex[slot]+1, slot

    vertical = grid[:,c]
    horizontal = grid[r]
    diag1 = Diag1(grid, r, c)  #\
    diag2 = Diag2(grid, r, c) #/

    return vertical, horizontal, diag1, diag2


def checkSlotToWin(grid, slotIndex):
    winSlot = []
    for slt in range(0,7):
        if slotIndex[slt] != -1:   #works?
            tempGrid = grid.copy()
            tempSltIndex = slotIndex.copy()
            tempGrid[slotIndex[slt]][slt] = 1
            tempSltIndex[slt] = tempSltIndex[slt] - 1
            leadWin = checkWin(tempGrid, slt, 1, tempSltIndex)
            if leadWin == True:
                #print(f"slot {slt + 1} will lead to a win")
                winSlot.append(slt)
    return winSlot

                

def checkSlotToThree(grid, slotIndex):
    threeSlot = []
    twoSlot = []
    for slt in range(0,7):
        if slotIndex[slt] == -1:
            continue
        tempGrid = grid.copy()
        tempSltIndex = slotIndex.copy()

        tempGrid[slotIndex[slt]][slt] = 1
        tempSltIndex[slt] = tempSltIndex[slt] - 1
        r, c = slotIndex[slt], slt
        #print(r, c)
        
        possibleWin = [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]
        possibleTwo = [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0]
        

        #Vertical
        vertical = tempGrid[:,slt]
        if r > 0 and r <= 3:
            if list(vertical[r-1:r+3]) == [0, 1, 1, 1]:
                threeSlot.append(slt)
        if r > 1 and r <= 4:
            #print(True)
            #print(list(vertical))
            if list(vertical[r-2:r+2]) == [0, 0, 1, 1]:
                twoSlot.append(slt)
                
                
        #Horizontal
        temp3 = []
        temp2 = []
        if slt <= 3:
            for i in range(0,slt+1):
                if list(tempGrid[r][slt-i:slt-i+4]) in possibleWin:
                    if slt not in temp3:
                        temp3.append(slt) 
                if list(tempGrid[r][slt-i:slt-i+4]) in possibleTwo:
                    if slt not in temp2:
                        temp2.append(slt)
                
        else:
            for i in range(0, 6-slt+1):
                if list(tempGrid[r][3-i: 3-i+4]) in possibleWin:
                    if slt not in temp3:
                        temp3.append(slt)
                if list(tempGrid[r][3-i: 3-i+4]) in possibleTwo:
                    if slt not in temp2:
                        temp2.append(slt)
        threeSlot = threeSlot + temp3
        twoSlot = twoSlot + temp2
        
        #slot = 0: horizontal[slot: slot + 4]
        #slot = 1: horizontal[slot: slot + 4] + horizontal[slot-1: slot-1+4]
        #slot = 2: horizontal[slot: slot + 4] + horizontal[slot-1: slot-1+4] + horizontal[slot-2: slot-2+4]

        #slot = 4: horizontal[3: 3+4] + horizontal[2: 2+4] + horizontal[1: 1+4]
        #slot = 5: horizontal[3: 3+4] + horizontal[2: 2+4]
        #slot = 6: horizontal[3: 3+4]

        #Diag1 #\
        diag1 = []
        for i in range(-3,4):
            tempr = r+i
            tempc = c+i
            if (tempr >= 0 and tempr <= 5) and (tempc >= 0 and tempc <= 6):
                diag1.append(grid[tempr, tempc])
        if any(diag1[i:i+4] in possibleWin for i in range(len(diag1) - 3)):
            threeSlot.append(slt)
        if any(diag1[i:i+4] in possibleTwo for i in range(len(diag1) - 3)):
            twoSlot.append(slt)

        #Diag2 #/
        diag2 = []
        for i in range(-3,4):
            tempr = r+i
            tempc = c-i
            if (tempr >= 0 and tempr <=5) and (tempc >= 0 and tempc <=6):
                diag2.append(grid[tempr, tempc])
        if any(diag2[i:i+4] in possibleWin for i in range(len(diag2) - 3)):
            threeSlot.append(slt)
        if any(diag2[i:i+4] in possibleTwo for i in range(len(diag2) - 3)):
            twoSlot.append(slt)

    return threeSlot, twoSlot
        




    
def checkWin(grid, slot, currentPlayer, slotIndex):
    #r, c = slotIndex[slot]+1, slot
    
    checkList = collect(grid, slot, slotIndex) 

    goalPoint = 4*currentPlayer
    for lists in checkList:
        if len(lists) >= 4:
            if any(np.sum(lists[i:i+4]) == goalPoint for i in range(len(lists) - 3)): #check any consecutive
                return True
    
        
    End = checkEnd(slotIndex)
    if End == True:
        return False
    return False

def checkThree(grid, opSlot, slotIndex, noList): #Check after opponentMove, whether they are getting a 3, and have to block
    r, c = slotIndex[opSlot]+1, opSlot
    possibleWin = [0, -1, -1, -1], [-1, 0, -1, -1], [-1, -1, 0, -1], [-1, -1, -1, 0]


    vertical, horizontal, diag1, _ = collect(grid, opSlot, slotIndex)
    #vertical = grid[:,c]  #horizontal = grid[r]  #diag1, start1 = Diag1(grid, r, c), r-c #\
    start1 = r-c
    diag2, start2 = Diag1(np.fliplr(grid), r, 6-c), r-(6-c) #/

    blockList = [] #block player from winning


    #Vertical  V
    if r > 0 and r <= 3 :
        if list(vertical[r-1:r+3]) == [0,-1,-1,-1]:        
            noList[opSlot].append(0)
    
    #Horizontal
    for i in range(len(horizontal)-3):
        tempList = list(horizontal[i:i+4])
        if tempList in possibleWin:
            zeroIndex = i+tempList.index(0) #zeroIndex = column
            noList[zeroIndex].append(slotIndex[zeroIndex] - r)
            #noList = updateNoList(noList, zeroIndex, (slotIndex[zeroIndex] - r))

    #Diag1 \
    if len(diag1) >= 4:
        #print(diag1)
        for i in range(len(diag1)-3):
            tempList = list(diag1[i:i+4])
            #print(tempList)
            if tempList in possibleWin:
                if start1 < 0:
                    zeroIndex = start1*-1 + i + tempList.index(0) #V
                    zr = i + tempList.index(0) #V
                else:
                    zeroIndex = i + tempList.index(0) #V
                    zr = start1 + i + tempList.index(0) #V

                noList[zeroIndex].append(slotIndex[zeroIndex]-zr)
                #noList = updateNoList(noList, zeroIndex, (slotIndex[zeroIndex] - zr)) #V
                    

    #Diag2 / Calculation check
    if len(diag2) >= 4:
        #print(diag2)
        for i in range(len(diag2)-3):
            tempList = list(diag2[i:i+4])
            #print(tempList)
            if tempList in possibleWin:
                if start2 < 0:
                    zeroIndex = 6-(start2*-1 + i + tempList.index(0)) #? #V
                    zr = i + tempList.index(0) #? #V
                else:
                    zeroIndex = 6-(i + tempList.index(0)) #? #V
                    zr = start2 + i + tempList.index(0) #? #V

                noList[zeroIndex].append(slotIndex[zeroIndex]-zr)
                #noList = updateNoList(noList, zeroIndex, (slotIndex[zeroIndex] - zr))
                
                #print(start2)

        
    #print(blockList)
    #print(f"noList after checkThree: {noList}")
    blockList = updateBlockList(blockList, noList)
    #print(f"blockList from noList: {blockList}")
    if blockList == []:
        return (None, noList)
    return blockList, noList
    


    
    

def Diag1(grid, r, c):
    diagList = []
    for i in range(-4,5):
        tempr = r+i
        tempc = c+i
        if (tempr >= 0 and tempr <= 5) and (tempc >= 0 and tempc <= 6):
            diagList.append(grid[tempr, tempc])
    return diagList

def Diag2(grid, r, c):
    diagList = []
    for i in range(-4,5):
        tempr = r+i
        tempc = c-i
        if (tempr >= 0 and tempr <= 5) and (tempc >= 0 and tempc <= 6):
            diagList.append(grid[tempr, tempc])
    return diagList



def checkEnd(slotIndex):
    finished = all( x == -1 for x in slotIndex )
    return finished

def updateNoList(noList, slot, value):
    noList[slot].append(value)
    return noList
    #if 0 add to block list, if 1 definitely dun put

def updateBlockList(blockList, noList):
    for i in range(0,7):
        if 0 in noList[i]:
            blockList.append(i)
    return blockList
    
