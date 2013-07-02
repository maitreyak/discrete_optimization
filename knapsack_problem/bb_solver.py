#!/usr/bin/python
# -*- coding: utf-8 -*-
values = [] 
weights = []
sorted_index = [] 
best_value = 0
best_list = ""

def linear_reduction(capacity,pointer):
    optimal_value = 0.0   
    
    for iterator in range(pointer,len(sorted_index)):
        
        index = sorted_index[iterator]
        
        if(capacity >= 0):
            balance = capacity - weights[index] 
            if(balance >= 0):
                optimal_value += values[index]
                capacity = balance
            else:
                part = weights[index]+ balance #as balance is alway <0
                part_value = part/float(weights[index])
                optimal_value += (part_value) * values[index]
                capacity = 0
        
        else:
            break
           
    return optimal_value

def branch(optimal_value,capacity,value,pointer,items):
    global weights
    global values
    global best_value
    global best_list
    global sorted_index

    #print optimal_value,best_value,value,capacity
    
   
    if(capacity < 0):
        return
   
    if(optimal_value<=best_value):
        return
    
    if(value > best_value):
        best_value = value
        best_list = items
    
    if(pointer >= len(values)):
        return

    item_index = sorted_index[pointer]
    item_weight = weights[item_index]
    item_value = values[item_index]
    
    #print "Branch taken opt:%r,value:%d,capacity:%d " %(optimal_value,value + item_value,capacity-(item_weight))
    branch(optimal_value,capacity-(item_weight),value + item_value,pointer+1,items+str(item_index)+" ")

    #item not taken
    new_opt_value = value + linear_reduction(capacity,pointer+1) 
    #print "Branch not taken %r" %new_opt_value
    branch(new_opt_value,capacity,value,pointer+1,items)


def solveIt(inputData):
    global values
    global weights
    global sorted_index
    sys.setrecursionlimit(100000)
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)
    
    value_to_weight_map = {}
    
    for x in range(0,items):
        value_to_weight_map[x] = (values[x]/float(weights[x]))
                
    sorted_vw = sorted(value_to_weight_map.items(), key=lambda x:x[1],reverse=True)
   
    for item in sorted_vw:
        sorted_index.append(item[0])

    init_opt_value = linear_reduction(capacity,0)
    
    branch(init_opt_value,capacity,0,0,"")
    
    outputData =  str(best_value)+' '+str(0)+'\n'
    #print best_list
    elements = best_list.split()
    for i in range(0,items):
        if(str(i) in elements):
            outputData+= str(1)+" "
        else:
            outputData+= str(0)+" "
            
    return outputData

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

