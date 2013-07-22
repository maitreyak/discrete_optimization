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
edges = []

#Methods the work on edges
def getLongEdge():
    global edges
    itemRange = len(edges)
    return max(range(itemRange),key = lambda index: approxLength(edges[index][0],edges[index][1]))

def makeRange(edge):
    global edges
    global xmap
    global ymap
    x1 = xmap[edges[edge][0]]
    x2 = xmap[edges[edge][1]]
    y1 = ymap[edges[edge][0]]
    y2 = ymap[edges[edge][1]]
    
    rangeX = []
    rangeY = []
    
    if(x1 < x2):
        rangeX = [x1,x2]
    else:
        rangeX = [x2,x1]
    
    if(y1 < y2):
        rangeY = [y1,y2]
    else:
        rangeY = [y2,y1]
    
    return rangeX,rangeY

def intersectEdge(edgeIndex):
    global edges
    global xmap
    global ymap
    
    mainRangeX , mainRangeY = makeRange(edgeIndex)

    for index in range(0,len(edges)):
        if index != edgeIndex:
             rangeX,rangeY= makeRange(index)
             
        if (mainRangeX[0]< rangeX[0] < mainRangeX[1]) or (mainRangeX[0]< rangeX[1] < mainRangeX[1]):
            if (mainRangeY[0]< rangeY[0] < mainRangeY[1]) or (mainRangeY[0]< rangeY[1] < mainRangeY[1]):
                    return index
            if (rangeY[0]< mainRangeY[0] < rangeY[1]) or (rangeY[0]< mainRangeY[1] < rangeY[1]):
                    return index

        if (rangeX[0]< mainRangeX[0] < rangeX[1]) or (rangeX[0]< mainRangeX[1] < rangeX[1]):
            if (mainRangeY[0]< rangeY[0] < mainRangeY[1]) or (mainRangeY[0]< rangeY[1] < mainRangeY[1]):
                    return index
            if (rangeY[0]< mainRangeY[0] < rangeY[1]) or (rangeY[0]< mainRangeY[1] < rangeY[1]):
                    return index

    return -1


def twoOpt():
    global edges   
    edge1 = getLongEdge()
    edge2 = intersectEdge(edge1)

    while(edge2 > 0):
        swpPoint = edges[edge1][1]
        edges[edge1][1] = edges[edge2][0]
        edges[edge2][0] = swpPoint
        print edges[edge1] 
        print edges[edge2]
        edge1 = getLongEdge()
        edge2 = intersectEdge(edge1)
    print edges


        
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
    #can control the quality of neigherhood search
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
    global edges
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
            edges.append([node,0])
        else:
            actualLenght += length(points[node],points[nextNode])
            edges.append([node,nextNode])
            node = nextNode
    
    return actualLenght    


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
    #output = str(actualLenght)+" 0\n"
    #output+= " ".join(map(str,visited))
    #output+="\n"
    #return output
    twoOpt()
    return ""


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


