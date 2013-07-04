#!/usr/bin/python
# -*- coding: utf-8 -*-

#initialize
def _init_(nodeCount,edgeCount):
    connectivity.nmap = {}
    node_value.nvalue = [0] * nodeCount
    

def node_value(node1,node2):
    node1 = int(node1)
    node2 = int(node2)

    node_value.nvalue[node1] += 1
    node_value.nvalue[node2] += 1



#method updates node connectivity, if the edge info is passed to it. 
def connectivity(node1,node2):
    node1 = int(node1)
    node2 = int(node2)
    if(node1 in connectivity.nmap):
        connectivity.nmap[node1].append(node2)
    else:
        connectivity.nmap[node1] = [node2]
    
    if(node2 in connectivity.nmap):
        connectivity.nmap[node2].append(node1)
    else:
        connectivity.nmap[node2] = [node1]

def solveIt(inputData):
       
    lines = inputData.split('\n')
    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])
    
    _init_(nodeCount,edgeCount)
    
    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        connectivity(parts[0],parts[1])
        node_value(parts[0],parts[1])
    
    return node_value.nvalue


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

