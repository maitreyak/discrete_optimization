#!/usr/bin/python
# -*- coding: utf-8 -*-

def solveIt(n):
    
    
    
    # Modify this code to run your puzzle solving algorithm
    
    # define the domains of all the variables (0..n-1)
    domains = [0]*n
    evenCount = 0
    oddCount =n-1    
    for index in range(0,n):
        if(index%2==0):
            domains[index] = int(evenCount)
            evenCount +=1
   
    for index in range(0,n):
        if(index%2!=0):    
            domains[index] = int(oddCount)
            oddCount -=1


    outputData = str(n) + '\n'
    outputData += ' '.join(map(str, domains))+'\n'
    
    return outputData

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
        print 'Solving Size:', n
        print(solveIt(n))

    else:
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python allIntervalSeriesSolver.py 5)')

