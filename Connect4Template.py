import numpy as np
#grid [6x[7]]

grid = [[1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]


Grid = np.array(grid)


board = [['O','O','O','.','X','X','O'],
         ['X','X','O','.','O','O','O'],
         ['X','X','X','O','X','O','O'],
         ['O','X','O','X','X','O','X'],
         ['X','O','O','X','O','X','X'],
         ['X','O','O','X','O','X','X']]


def printGrid(givenGrid):
    print(givenGrid)

def printBoard(givenBoard):
    printAs = "\n".join(f"| {" ".join(row)} |" for row in givenBoard)
    return printAs

print(printBoard(board))
print("Well Done, you beat me")



#Case 1, said Well Done after I put slot 4
"""
grid = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,-1,-1,-1,0,0],
        [0,0,1,-1,1,0,0],
        [0,1,1,-1,-1,-1,1]]

board = [   0  -1  -2  -3  -4  -5  -6
         0['.','.','.','.','.','.','.'],
         1['.','X','.','.','.','.','.'],
         2['.','O','.','X','.','.','.'],
         3['X','O','O','O','.','O','.'],
         4['O','O','X','O','.','X','.'],
         5['X','X','O','X','X','X','O']]

board = [   0  -1  -2  -3  -4  -5  -6
         0['.','.','.','.','.','.','.'],
         1['.','.','O','.','.','.','.'],
         2['.','O','.','X','.','.','.'],
         3['.','.','O','.','O','.','.'],
         4['.','.','.','X','.','O','.'],
         5['.','.','.','.','O','.','.']]

board = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','O'],
         ['.','.','.','.','O','X','.'],
         ['.','.','.','O','O','.','.'],
         ['.','.','X','O','.','.','.'],
         ['.','O','.','.','.','.','.']]
         
boardFlip = [['.', '.', '.', '.', '.', '.', '.'],
             ['O', '.', '.', '.', '.', '.', '.'],
             ['.', 'X', 'O', '.', '.', '.', '.'],
             ['.', '.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', 'O', 'X', '.', '.'],
             ['.', '.', '.', '.', '.', 'O', '.']]
         

SlotIndex = [5, 4, 2, 1, 2, 4, 4]

"""

#V means done
#Test if removing blockList.append statement works correctly  V?
#See if I can remove the whole blockList, i think can    V all #ed
#find out the correct diag zr,zc calculation V
#the same column, cant block twice, noList value got reset  V
    #noList = [[0,1,3],[],[]], any(noList[slot] == 0)

#FindBestSlot logic should check if a slot can lead to win first  V
#Do a for loop for each slot and checkWin? V

#allow user to type in string without crashing the game

#Work on Evaluation Function now  \
#!!! debug [0,0,2000,2000,34000,0,0] but noList is 4 V
#debug on maxScore
#is 4,3,2 enough, need some kind of strategies?
#do we need checkWin(winSlot) first, then win score again in evaluate ##as long as they are somewhere to make sure that the win slot will be definitely prioritised


#AlphaBetaPrun
#branches only to max score? or all that's != 0
#until third layer, pick the branch gives max score?
#Search for existing code/template



"""
should my evaluation function be the sum of the noList values?
will that works?
Or i need some more complicated calculation function?
connected 2 should be examinated as well
"""

