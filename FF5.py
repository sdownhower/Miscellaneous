# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:44:42 2020

@author: Stephen Downhower
"""

import time

triangleExample = [3,
                   7,4,
                   2,4,6,
                   8,5,9,3]

def flattenTwoLevels(level1, level2):
    '''Calculates the path sums for two levels and groups the path sums by node'''
    
    flattened = [[]]
    
    # Handles inital case with first level of size one
    if len(level1) == 1:
        return [[level1[0] + level2[0]], [level1[0] + level2[1]]]
    
    # Handles cases with first level of size greater than one
    else:
        for node_idx in range(len(level1)):  
            # Moving from right-to-left calculates the path sums of the level 
            #   one parent nodes with their right child node
            for elem in level1[-1]:
                flattened[0].append(elem + level2[-1])
            
            # Remove right child node in order to move on to left
            del level2[-1]
            
            # Moving from right-to-left calculates the path sums of the level 
            #   one parent nodes with their left child node
            if len(level2) > 0:
                flattened.insert(0,[])
                for elem in level1[-1]:
                    flattened[0].append(elem + level2[-1])
                    
            # Remove right parent node in order to move to the left
            del level1[-1]
            
    return flattened
        
def findTriangleMax(triangle):
    '''Takes a triangle encoded as a list of integers and finds the maximum 
    path sum down the length of the triangle'''
    
    # Determine number of levels in the tree and restructure the data into a list
    #   of lists where each nested list represents a level
    levels = 1
    currentLength = len(triangle)
    treeArray = []
    while True:
        currentLength = currentLength - levels
        if currentLength == 0:
            treeArray.append(triangle[0:levels])
            break
        elif currentLength < 0:
            return "Error: input is not a triangle"
        else:
            treeArray.append(triangle[0:levels])
            del triangle[0:levels]
            levels = levels + 1

    # Goes through the levels of the tree in pairs
    #   After a pair is "flattened" the path sums at each node are returned
    #   Continues flattening and calculating path sums until it reaches the last pair of levels
    flattened = []
    flattened.append(flattenTwoLevels(treeArray[0], treeArray[1]))
    for i in range(levels - 2): 
        flattened.append(flattenTwoLevels(flattened[-1], treeArray[i + 2]))

    # Finds the max value in each node and then returns the max value found in
    # all nodes
    nodeMaxes = []
    for i in range(len(flattened[-1])):
        nodeMaxes.append(max(flattened[-1][i]))
        
    return max(nodeMaxes)
        

if __name__ == '__main__':
    start = time.time()
    maxValue = findTriangleMax(triangleExample) # Feel free to plug in a different triangle array here
    finish = time.time() - start
    print('Triangle Example Calculation: ' + str(maxValue))
    print('Calculated in ' + str(finish) + ' s')