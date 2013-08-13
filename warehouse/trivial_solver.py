#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from collections import deque
warehouseCount = 0
customerCount = 0
warehouses = []
customerSizes = [] 
customerCosts = []
sortedCosts= []
wCapacity =[]
wCost = []
wcMap = {}
openMap = {}
custMap ={}
sortedDistance = []
custAssoCount = 0
sortedTotalCost = [] 
minVal = 1000000000.0
minWc = []

def sortCustomerCosts():
    global sortedCosts
    for i in range(0,customerCount):
        sortedCosts.append(sorted(range(0,warehouseCount),key = lambda index: customerCosts[i][index]))


def sortTotalCost():
    global sortedTotalCost 
    for i in range(0,warehouseCount):
        cost = 0.0
        for j in range(0,customerCount):
            cost = cost + customerCosts[j][i]
        cost += warehouses[i][1]
        sortedTotalCost.append(cost)


def sortWarehousetoCust():
    global sortedDistance
    for i in range(0,warehouseCount):
        sortedDistance.append(sorted(range(0,customerCount),key = lambda index: customerCosts[index][i]))

def pickWarehouse(customer):
    global wCapacity
    global wcMap
    
    costList = sortedCosts[customer]

    for warehouse in costList:
        #check if open
        if openMap[warehouse] == False:
            continue
        #check capacity
        if wCapacity[warehouse] < customerSizes[customer]:
            continue
        else:
            if warehouse in wcMap: 
                wcMap[warehouse].append(customer)
            else:
                wcMap[warehouse] = [customer]
            
            wCapacity[warehouse] -= customerSizes[customer]
            return True
    
    return False

    
def greedy():
    global sortedTotalCost
    global wCapacity
    global wcMap
    global minVal
    global minWc
    global openMap
    
    sortCustomerCosts()
    sortTotalCost()
   
    demandList = sorted(range(0,warehouseCount),key = lambda index:sortedTotalCost[index])
    
    revertCapacity = list(wCapacity)     
    for i in range(0,warehouseCount): 
        for index in range(0,warehouseCount/3):        
            openMap[demandList[index]] = True       
            for customer in range(0,customerCount):
                pickWarehouse(customer)
            
            tempVal= calculate()
            if(tempVal< minVal):
                minVal=tempVal
                minWc = copy.deepcopy(wcMap)
            
            wCapacity = list(revertCapacity)
            wcMap = {}
        
        for x in range(0,warehouseCount):
            openMap[x]= False
        
        queue= deque(demandList)   
        element = queue.popleft()
        queue.append(element)
        demandList = list(queue)

    wcMap = minWc
        
def pickCustomers(warehouse,fraction):
    
    global openMap
    global wCapacity
    global wcMap
    global custAssoCount
    global custMap 
    #Mark the warehouse open
    count =0
    openMap[warehouse] = True
    distaceList = sortedDistance[warehouse]

    for customer in distaceList:
        if custMap[customer] == True:
            continue
        if wCapacity[warehouse] < customerSizes[customer]:
            continue
        else:
            if warehouse in wcMap: 
                wcMap[warehouse].append(customer)
            else:
                 wcMap[warehouse] = [customer]
            
            custMap[customer] = True
            custAssoCount+=1
            wCapacity[warehouse] -= customerSizes[customer]
            count+=1
            if(count >=customerCount/fraction):
                return

def calculate():
    objectValue = 0.0
    for warehouse, custList in wcMap.items():
        objectValue+=wCost[warehouse]        
        for cust in custList:
            objectValue += customerCosts[cust][warehouse]      
    return objectValue

def formatList():
    #print wCapacity
    returnList = [0] * customerCount
    for warehouse, custList in wcMap.items():
        for cust in custList:
            returnList[cust] = warehouse                             
    
    return returnList 

def solveIt(inputData):
    
    global warehouseCount
    global customerCount
    global warehouses
    global customerSizes
    global customerCosts
    global wCapacity
    global wCost
    global openMap

    lines = inputData.split('\n')

    parts = lines[0].split()
    warehouseCount = int(parts[0])
    customerCount = int(parts[1])

    warehouses = []
    for i in range(1, warehouseCount+1):
        line = lines[i]
        parts = line.split()
        warehouses.append((int(parts[0]), float(parts[1])))
        wCapacity.append(int(parts[0]))
        wCost.append(float(parts[1]))
        openMap[i-1] = False

    customerSizes = []
    customerCosts = []

    lineIndex = warehouseCount+1
    for i in range(0, customerCount):
        customerSize = int(lines[lineIndex+2*i])
        customerCost = map(float, lines[lineIndex+2*i+1].split())
        customerSizes.append(customerSize)
        customerCosts.append(customerCost)
        custMap[i] = False

    sortWarehousetoCust()
    greedy()
    output = str(calculate())+" 0\n"
    output+= " ".join(map(str,formatList()))
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
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/wl_16_1)'

