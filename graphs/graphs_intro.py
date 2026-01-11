

# Ways of representing graphs

# Type 1 : Matrix
# Eg Matrix

from typing import List


def matrixDefintion():
    matrix:List[List[int]] = [[0,0,0,0]
                              [1,1,0,0]
                              [0,1,0,0]]
    # In these 0 represents nodes and 1 represents blocked path 
    #all the zeros are nodes
    return 0

def adjancencyMatrix():
    matrix:List[List[int]] = [[0,0,0,0]
                              [1,1,0,0]
                              [0,1,00,0]]
    # matrix[v1][v2] = 1 means and edge exists bw v1 -> v2
    # this method is rarely used as it takes more space complexity
    

    return 0


#Type 3: Adjancency List represntations More Space Effiencient than type 2
class GraphNode():

    def __init__(self,val):
        self.val  = val
        #contains pointers / ref of the neighbors
        self.neighbours =[]