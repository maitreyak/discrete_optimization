#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

points = [] 
visited = []
visitedMap = {}
xlist = [] 
ylist =[]
xmap = {}
ymap = {}


#Helper method of actual distance calulation 
def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#Helper method for approx length
def approxLength(point1, point2):
    point1 = points[point1]
    point2 = points[point2]
    return abs(point1[0] - point2[0])+abs(point1[1] - point2[1])

def nearestElementPrereqs():
    global points
    global xlist
    global ylist
    global xmap
    global ymap
    
    nearestElement.count = 0

    itemRange = len(points)
    xlist = sorted(range(itemRange), key= lambda x: points[x][0])
    ylist = sorted(range(itemRange), key= lambda y: points[y][1])
    
    for index in range(0,itemRange):
        xmap[xlist[index]] = index
        ymap[ylist[index]] = index

def nearestElement(node):
    global vistedMap
    #nearestElement.count= nearestElement.count+1
    #print nearestElement.count
    k=20000
    itemRange = len(points)

    xMean = xlist[xmap[node]]
    yMean = xlist[ymap[node]]

    x1 = xMean-1
    x2 = xMean+1

    y1 = yMean-1
    y2 = yMean+1
    
    xpoints = {} 
    ypoints = {} 

    candidates= [] 

    while len(candidates) <=k:

        if x1<0 and x2>=itemRange and y1<0 and y2 >=itemRange:
            break
        if x1 >= 0:
            if not (xlist[x1] in visitedMap):
                xpoints[xlist[x1]] = True
        if x2 <itemRange:
            if not (xlist[x2] in visitedMap):        
                xpoints[xlist[x2]] = True
        
        if y1 >= 0:
            if not (ylist[y1] in visitedMap):    
                ypoints[ylist[y1]] = True
        if y2 <itemRange:
            if not (ylist[y2] in visitedMap):
                ypoints[ylist[y2]] = True
       
       # candidates = set(xpoints).intersection(set(ypoints))
        if x1 >=0 and xlist[x1] in ypoints:
            candidates.append(xlist[x1])
           
        if x2<itemRange and xlist[x2] in ypoints:
            candidates.append(xlist[x2])
           
        if y1 >=0 and ylist[y1] in xpoints:
            candidates.append(ylist[y1])

        if y2<itemRange and ylist[y2] in xpoints:
            candidates.append(ylist[y2])
        
        x1-=1
        x2+=1
        y1-=1
        y2+=1


    if len(candidates) > 0:
        return min (candidates,key = lambda x:approxLength(x,node))
    else:
        return -1    


#Greedy algo for the tsp graph
def greedyTsp():
    global visited
    global vistedMap
    node = 0
    nextNode = 0
    noCircuit = True
    actualLenght = 0.0
    
    while(noCircuit):
        visited.append(node)
        visitedMap[node] =True

        nextNode =  nearestElement(node)
        
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

    nearestElementPrereqs()
    #build tsp solution using greedy approach
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


