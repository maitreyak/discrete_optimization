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
    print_chessboard(queens,param['N'])
    #print 'Nodes:', solver.getNodes(), ' Time:', solver.getTime()

def print_chessboard(queens,N):
    #separator = '+---'*len(queens)+'+'
    #output = ""
    print N
    print " ".join(map(str,queens))
    #for queen in queens:
    #    output= queen
        #print '|   '*queen.get_value()+'| Q |'+'   |'*(len(queens)-1-queen.get_value())
    #print separator

solve_queens(input({'solver':'Mistral', 'N':500}))
