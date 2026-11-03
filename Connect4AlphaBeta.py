import copy
import Connect4CheckState as Check
import Connect4Evaluate as Eval

# alpha - maximiser's guaranteed lower bound
# beta - minimiser's guaranteed upper bound
# maxEval - the max board_score for this node

#Prune when the move scored higher then what the minimiser is willing to allow
def AlphaBeta (grid, depth, alpha, beta, Player, slotIndex, noList, last_slot):

    if last_slot is not None and Check.checkWin(grid, last_slot, -1*Player, slotIndex):
        return -100000 + depth*100, None
    #Base case, start with 0: 
    if depth == 3 or Check.checkEnd(slotIndex):
        board_score, _ = Eval.evaluate(grid, slotIndex, noList)
        return board_score, None

    best_slot = None

    if Player == 1: #AI
        maxEval = -float('inf') 

        for slt in range(0,7):
            if slotIndex[slt] != -1:
                tempGrid = copy.deepcopy(grid)
                tempSltIndex = copy.deepcopy(slotIndex)
                tempGrid[slotIndex[slt]][slt] = 1
                tempSltIndex[slt] = tempSltIndex[slt] - 1
                board_score, _ = AlphaBeta(tempGrid, depth+1, alpha, beta, Player*-1, tempSltIndex, noList, slt)
                
                #Check if this move is better than our previous best
                if board_score > maxEval:
                    maxEval = board_score
                    best_slot = slt
                
                alpha = max(alpha, maxEval)
                #Pruning: If score is greater than or equal to Beta, cut the branch
                if alpha >= beta:
                    break
        
        return maxEval, best_slot
    elif Player == -1:
        minEval = float('inf')
        for slt in range(0, 7):
            if slotIndex[slt] != -1:
                tempGrid = copy.deepcopy(grid)
                tempSltIndex = copy.deepcopy(slotIndex)
                tempGrid[tempSltIndex[slt]][slt] = -1
                tempSltIndex[slt] = tempSltIndex[slt] -1
                board_score, _ = AlphaBeta(tempGrid, depth+1, alpha, beta, Player*-1, tempSltIndex, noList, slt)

                if board_score < minEval:
                    minEval = board_score
                    best_slot = slt

                beta = min(beta, minEval)

                if beta <= alpha:
                    break
        return minEval, best_slot