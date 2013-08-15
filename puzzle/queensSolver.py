#!/usr/bin/python
# -*- coding: utf-8 -*-

from Numberjack import *

def model_queens(N):
    queens = [Variable(N) for i in range(N)]
    model  = Model( 
        AllDiff( queens ),
        AllDiff( [queens[i] + i for i in range(N)] ),
        AllDiff( [queens[i] - i for i in range(N)] ) 
        )
    return (queens,model)

def solve_queens(param):
    (queens,model) = model_queens(param['N'])
    solver = model.load(param['solver'])
    solver.solve()
    return print_chessboard(queens,param['N'])
    
    #print 'Nodes:', solver.getNodes(), ' Time:', solver.getTime()

def print_chessboard(queens,N):
    output= str(N)+"\n"
    output+=" ".join(map(str,queens))
    return output  



def solveIt(n):
   return  solve_queens(input({'solver':'Mistral', 'N':n}))



import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
       # print 'Solving Size:', n
        print(solveIt(n))

    else:
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python queensSolver.py 8)')

