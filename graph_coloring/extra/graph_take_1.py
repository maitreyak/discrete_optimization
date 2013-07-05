#!/usr/bin/python
# -*- coding: utf-8 -*-

#initialize
def _init_(node_count,edge_count):
    connectivity.nmap = {}
    node_value.nlist = [0] * node_count
    domain.nono_color = {}

#Calculates the node values
def node_value(node1,node2):
    node1 = int(node1)
    node2 = int(node2)

    node_value.nlist[node1] += 1
    node_value.nlist[node2] += 1

#Sort the index based on the node value list
def sorted_index(nlist):
    sorted_index.nindex = sorted(range(len(nlist)), key=lambda k:nlist[k],reverse=True)


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


def pick_color(index):
    if (index in domain.nono_color):
        nono_list = domain.nono_color[index]
        for value in range(0,max(nono_list)+1):
            if(value not in nono_list):
                return value
        
        return max(nono_list)+1
    
    else:
        return 0    


def domain(index,color):
    connected = connectivity.nmap[index] 
    for item in connected:
        node_value.nlist[item] += -1 

        if(item in domain.nono_color):
            domain.nono_color[item].add(color)
        else:
            domain.nono_color[item] = set([color])
    

#Constraint progarmming Jargon, bascially the main loop. 
def fixed_point_loop():
    
    elements = len(node_value.nlist)
    color_index = [-1] * len(node_value.nlist)
    
    for i in range(0,elements):
                       
        element_index  = max(enumerate(node_value.nlist), key= lambda x: x[1])[0]
        #Assign the color to the element          
        color = pick_color(element_index)
        color_index[element_index] = color
        #Recalculate the domain
        domain(element_index,color)
        node_value.nlist[element_index] = -1    
        
    #for domain(element_index,color)       element_index in sorted_index.nindex:
    #   #Assign the color to the element
    #   color = pick_color(element_index)
    #   color_index[element_index] = color
    #   #Recalculate the domain
    #   domain(element_index,color)
        
    return color_index


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
   
    sorted_index(node_value.nlist)
    
    #print connectivity.nmap 
    #print node_value.nlist
    #print sorted_index.nindex
    finallist = fixed_point_loop()
    output = str(max(finallist)+1)+" 0\n"
    output+= " ".join(map(str,finallist))
    
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
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

