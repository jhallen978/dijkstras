'''
Implementation of Dijkstra's shortest path algorithm

@author: Jonathan Allen

'''

import sys

'''
Generates the shortest path from startingVertex to all  other
vertices specified in the graph in inputFile.
'''
def main(inputFile, startingVertex):
    '''
    input file containing directed-graph with positive weights
    
    file contents is
    [begin vertex] [end vertex] [cost]
    '''
    graph = open(inputFile)

    '''
    an initially empty dictionary containing mapping
    [vertex]:[adjacency list]
    '''
    adjacency = { }
    
    '''
    The following reads in the input file
    and constructs an adjacency list of
    the graph.
    '''
    for line in graph:
        entry = line.split()
        
        if entry[0] not in adjacency:
            adjacency[entry[0]] = []
           
        # construct an edge for the adjacency list
        edge = (entry[1], int(entry[2]))
        adjacency[entry[0]].append(edge)

    '''
    output the adjacency list 
    '''

    for v in adjacency:
        print(v, adjacency[v])

    '''
    YOUR LOGIC WILL GO HERE
    '''
    distance = {}
    previous = {}
    unvisited = []
    current = startingVertex
    for v in adjacency:
        distance[v] = float("inf")
        unvisited.append(v)
    
    for v in unvisited:
        if v in adjacency:
            for x in adjacency[v]:
               
                if x[0] not in unvisited:
                    unvisited.append(x[0])
                    distance[x[0]] = float("inf")
  
    distance[startingVertex] = 0
    while(unvisited):
        unvisited.remove(current)
       
        while(adjacency[current]):    
            temp = adjacency[current].pop()
            if distance[temp[0]] > (temp[1] + distance[current]):
                distance[temp[0]] = temp[1] + distance[current]
                previous[temp[0]] = current
        min = float("inf")
        nextVertexNotFound = True
        while(nextVertexNotFound and unvisited):
            #print((min > distance[v]) and (v in unvisited))
            for v in distance:
                if ((min > distance[v]) and (v in unvisited)):
                    if v in adjacency:
                        
                        min = distance[v]
                        current = v
                        nextVertexNotFound = False
                    else:
                        unvisited.remove(v)
                        nextVertexNotFound = True
                        min = float("inf")
    print(distance)
    print(previous)
if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print('Usage python shortestpath.py [input file] [starting vertex]')
        quit()
        
    main(sys.argv[1], sys.argv[2])
