# one type to define graphs
class GraphNode:
    def __init__(self,val):
        self.val  =val
        self.neighbors = []

# better way is to represent by hashmaps, key is the
#value of node and value is the neighbors

adjList = {"A":[], "B":[]}

edges = [["A","B"],["B","C"],["B","E"],["C","E"],["E","D"]]
        