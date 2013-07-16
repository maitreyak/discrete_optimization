#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

points = [] 
distaceMatrix = []
visited = [] 

#Helper method of actual distance calulation 
def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#Helper method for approx length
def approxLenght(point1, point2):
    return abs(point1[0] - point2[0])+abs(point1[1] - point2[1])

#Build the distance matrix
def buildDistanceMatrix():
    global distaceMatrix
    global points
    for i in range(0,len(points)):
        jaxis = [] 
        for j in range(0,i):
            jaxis.append(approxLenght(points[i],points[j]))
        
        distaceMatrix.append(jaxis)

#helper method for point to point distance.
def distance(point1,point2):
    global distanceMatrix
    if(point1 == point2 ):
        return 0
    elif (point1 > point2):
        return distaceMatrix[point1][point2]
    else:
        return distaceMatrix[point2][point1]

#Greedy algo for the tsp graph
def greedyTsp():
    global visited
    visited.append(0)
    node = 0
    nextNode = 0
    noCircuit = True
    actualLenght = 0.0
    
    while(noCircuit):
        nextNode =  closeNode(node)
        
        #End loop
        if nextNode < 0:
            noCircuit = False
            actualLenght += length(points[node],points[0])
        else:
            actualLenght += length(points[node],points[nextNode])
            node = nextNode
        
    return actualLenght    

#closest point
def closeNode(nodeIndex):
    minValue = 0 
    minIndex = 0
    global visited 
    for index in range(0,len(points)):
        if index != nodeIndex and index not in visited:
            if minValue == 0: 
                minValue= distance(nodeIndex,index)
                minIndex = index
            else:
                if minValue > distance(nodeIndex,index):
                    minValue = distance(nodeIndex,index)
                    minIndex = index
                        
    if(minValue == 0):
        return -1
    else:
        visited.append(minIndex)
        return minIndex


#Test menthods
def printMatrix():
    global distaceMatrix
    global points
    for i in range(0,len(points)):
        for j in range(0,len(points)):
            print distance(i,j),"  ",i,"-",j
        print ""


def solveIt(inputData):
    global points  
    lines = inputData.split('\n')
    nodeCount = int(lines[0])

    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append((float(parts[0]), float(parts[1])))

    #build tsp solution using greedy approach
    buildDistanceMatrix()
    actualLenght = greedyTsp()
    output = str(actualLenght)+" 0\n"
    output+= " ".join(map(str,visited))
    return output 


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'


