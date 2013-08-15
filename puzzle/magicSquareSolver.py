#!/usr/bin/python
# -*- coding: utf-8 -*-
from Numberjack import *

def model_magic_square(N):
    sum_val = N*(N*N+1)/2 # This is what all the columns, rows and diagonals must add up tp

    square = Matrix(N,N,1,N*N)
    model = Model(
            AllDiff( square.flat ),
        
            [Sum(row) == sum_val for row in square.row],
            [Sum(col) == sum_val for col in square.col],
            
            Sum([square[a,a] for a in range(N)]) == sum_val,
            Sum([square[a,N-a-1] for a in range(N)]) == sum_val,
            [square[a,a] > square[a-1,a-1]  for a in range(1,N)]
            )
    return (square,model)

    
def solve_magic_square(param):
    (square,model) = model_magic_square(param['N'])
    solver = model.load(param['solver'])
    output = str(param['N'])+" \n"
    
    if solver.solveAndRestart():
        #print square
        length = len(square)
        for i in range(0,len(square)):
            elements =" ".join(map(str,square[i]))
            output += elements +"\n"
                   
    return output
    #print 'Nodes:', solver.getNodes(), ' Time:', solver.getTime()

def solveIt(n):
    outputData = solve_magic_square(input({'solver':'Mistral', 'N':n}))
   
    
    return outputData




import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
        #print 'Solving Size:', n
        print(solveIt(n))
    
    else:
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python magicSquareSolver.py 3)')

