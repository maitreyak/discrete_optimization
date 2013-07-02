#!/usr/bin/python
# -*- coding: utf-8 -*-
subProblemMap = {}
values = []
weights = []

def dynamicProgramming(items,capacity):
    global subProblemMap 
    global weights
    global values

    if items <= 0 or capacity <=0: 
       subProblemMap[items,capacity] = 0
       return 0
    if items == 1:
        if weights[0]<= capacity:
            subProblemMap[items,capacity] = values[0]
            return values[0]
        else:
            subProblemMap[items,capacity] = 0
            return 0
    
    key1 = ":".join(str(x) for x in [items-1,capacity])
    key2 = ":".join(str(x) for x in [items-1,capacity-weights[items-1]])
    
    dpValue1 = 0
    dpValue2 = 0

    #print "Looking for key1 %s and key2 %s in the subprob map" %(key1,key2)
    
    if(key1 in subProblemMap):
        dpValue1 = subProblemMap[key1]
        #print "its a hit key1"
    else:
        dpValue1 =  dynamicProgramming(items-1,capacity)
        ##update map
        subProblemMap[key1] = dpValue1
    
    if(capacity-weights[items-1] >0):
        if(key2 in subProblemMap):
            dpValue2 = subProblemMap[key2]
            #print "its a hit key2"
        else:
            dpValue2 =  dynamicProgramming(items-1,capacity-weights[items-1])
            ##update the map
            subProblemMap[key2] = dpValue2
         
        dpValue2 = dpValue2 + values[items-1]
    
    #Now for the actual return value
    finalValue = max(dpValue1,dpValue2)
    #print items,"--->",capacity,":value",finalValue
    return finalValue


def solveIt(inputData):

# parse the input
    global values
    global weights
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)
    sys.setrecursionlimit(100000)
    result = dynamicProgramming(items,capacity)
    subProblemMap[str(items)+":"+str(capacity)] = result
    
    printStr = str(result)+" "+str(1)+"\n"
    printStr+= traceIt(items,capacity,result)
    return printStr

def traceIt(items,capacity,result):
    global subProblemMap
    global values
    global weights
    taken = [] 
    while(items>0):
        key1 = str(items)+":"+str(capacity)
        key2 = str(items-1)+":"+str(capacity)
        
        if(key1 in subProblemMap):
            cell = subProblemMap[key1]
        else:
            cell = 0
        if(key2 in subProblemMap):
            adj_cell = subProblemMap[key2]
        else:
            adj_cell = 0
        
        if(cell==adj_cell):
            taken.append(0)
            cell = adj_cell
        else:
            taken.append(1)
            capacity = capacity - weights[items-1]
            if(capacity <0):
                capacity = 0
                
        items = items -1
    
    return " ".join(map(str,reversed(taken)))
    

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

