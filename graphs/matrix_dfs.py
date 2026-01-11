    
from typing import List


matrix:List[List[int]] = [[0,0,0,0]
                         [1,1,0,0]
                        [0,0,0,1],
                        [0,1,0,0]]




# TC - o( 4^(nm)) SC - O(nm)
def dfs(stRow:int,stCol:int,graph:List[List[int]],visit:List[tuple]):

    if stRow>len(graph) or stRow<0:
        return 0
    
    if stCol>len(graph[0]) or stCol<0:
        return 0
    
    if graph[stRow][stCol] ==1:
        return 0

    if (stRow,stCol) in visit:
        return 0
    
    count =0

    visit.append((stRow,stCol))
    count += dfs(stRow+1,stCol,graph,visit)
    count+=dfs(stRow-1,stCol,graph,visit)
    count+=dfs(stRow,stCol-1,graph,visit)
    count+=dfs(stRow,stCol+1,graph,visit)
    visit.remove((stRow,stCol))

    return count
    





    return 0
def matrixDfs():






    return 0


