#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
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
minObjective = 0.0

def sortCustomerCosts():
    global sortedCosts
    for i in range(0,customerCount):
        sortedCosts.append(sorted(range(0,warehouseCount),key = lambda index: customerCosts[i][index]))

def pickWarehouse(customer):
    global openMap
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
    global minObjective
    demandList = sorted(range(0,customerCount),key = lambda index:customerSizes[index],reverse = True)
    for index in demandList:
        pickWarehouse(index)
    
    minObjective = calculate()


def shutdownW(warehouse):
    global wcMap
    global wCapacity
    global minObjective
    
    localWcMap = copy.deepcopy(wcMap)
    localWCapcity = copy.deepcopy(wCapacity)
    
    feasible = True
    
    if warehouse not in wcMap:
        return False 
    
    openMap[warehouse] = False    
    custList = wcMap[warehouse][:]
    for cust in custList:
        if pickWarehouse(cust) == False:
            feasible = False
            break
    
    if feasible == False:
        wcMap = localWcMap
        wCapacity = localWCapcity
        openMap[warehouse] = True
        return False
    else:
        wcMap[warehouse] = []
        del wcMap[warehouse]
        value = calculate()
        if value >= minObjective:
            wcMap = localWcMap
            wCapacity = localWCapcity
            openMap[warehouse] = True
            return False
        else:
            minObjective = value
            return True

def closeAndMove():
   # count = 10
   # for index in range(0,count):
    wlist= sorted(range(0,warehouseCount),key = lambda index:warehouses[index][1]/warehouses[index][0],reverse =True)    
    for warehouse in wlist:
        if openMap[warehouse] == True:
            shutdownW(warehouse)


def calculate():
    objectValue = 0.0
    for warehouse, custList in wcMap.items():
        objectValue+=wCost[warehouse]        
        for cust in custList:
            objectValue += customerCosts[cust][warehouse]      
    return objectValue

def formatList():
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
        openMap[i-1] = True

    customerSizes = []
    customerCosts = []

    lineIndex = warehouseCount+1
    for i in range(0, customerCount):
        customerSize = int(lines[lineIndex+2*i])
        customerCost = map(float, lines[lineIndex+2*i+1].split())
        customerSizes.append(customerSize)
        customerCosts.append(customerCost)

    sortCustomerCosts()
    greedy()
    closeAndMove()
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

