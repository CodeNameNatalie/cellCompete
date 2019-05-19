"""
Eight houses, represented as cells, are arranged in a straight line.
Each day every cell comptetes with its adjacent cells.  An int value of 1
represents an active cell and a value of 0 represents an inactive cell.
If the neighbors on both sides are active or if they are both inactive,
the cell becomes inactive the next day, else it becomes active.  The 
two cells on each end have a single adjacent cell, so assume that the
unoccupied space on the opposite side is an inactive cell.  Even after
updating the cell state, consider its previous state when updating the state
of other cells.  The state info of all cells should be updated simultaneously.

Write an algorithm to output the state of the cells after the given number of days

states = list of ints (either 0s or 1s)
days = int

def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    #active=1 inactive=0
    #1X1 then X=1, 1X0 then X=0, 0X1 then X=0, 0X0 then X=1
    #list is only 0s and 1s
    num = len(states)
    temp=states[:]
    
    #when only 1 node
    if num==1: print[0]
    for _ in range(days):
        #edge nodes first
        temp[0] = states[1]
        temp[num-1] = states[num-2]
        
        for i in range(1, num-1):
            #rest of the nodes
            temp[i] = 1-(states[i-1]==states[i+1])
        #update states
        states = temp[:]
    return temp
