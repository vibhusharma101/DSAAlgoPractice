class Heap:
    #fChild = 2*i
    #sChild = 2*i+1
    #parent  = i/2
    # below is the min heap
    #[0,14,16,61,19]
    def __init__(self):
        self.heap =[0]
    
    # time complexity - O ( logn )
    def push(self,val):
        self.heap.append(val)
        cIndex = len(self.heap)-1

        while self.heap[cIndex]<self.heap[cIndex//2]:
            self.heap[cIndex], self.heap[cIndex//2] =  self.heap[cIndex//2],  self.heap[cIndex]
            cIndex = cIndex//2
    



    def push2(self,val):
        self.heap.append(val)
        currIndex = len(self.heap)-1
        while currIndex>0:
            if self.heap[currIndex//2]>self.heap[currIndex]:
                self.heap[currIndex//2],self.heap[currIndex] = self.heap[currIndex], self.heap[currIndex//2]
                currIndex = currIndex//2
            else:
                break
        
    # Tcomplexity is O(logn)
    def pop(self):
        self.heap[1] = self.heap.pop()
        cIndex = 1

        while 2*cIndex<len(self.heap):
            if 2*cIndex+1<len(self.heap) and self.heap[cIndex]>self.heap[2*cIndex+1] and self.heap[2*cIndex]>self.heap[2*cIndex+1]:
                self.heap[cIndex]+self.heap[2*cIndex+1] = self.heap[2*cIndex+1], self.heap[cIndex]
                cIndex = 2*cIndex+1
            elif self.heap[cIndex]>self.heap[2*cIndex]:
                self.heap[cIndex],self.heap[2*cIndex] = self.heap[2*cIndex],self.heap[cIndex]
                cIndex = 2*cIndex
            else:
                break
    

    # replae the root with last element
    def pop2(self):
        self.heap[0] = self.heap.pop()
        currIndex = 0

        while currIndex<len(self.heap):
            if 2*currIndex+1<len(self.heap) and self.heap[2*currIndex+1]<self.heap[2*currIndex] and self.heap[2*currIndex+1]<self.heap[currIndex]:
                self.heap[currIndex],self.heap[2*currIndex+1] = self.heap[2*currIndex+1],self.heap[currIndex]
                currIndex = 2*currIndex+1
            elif 2*currIndex<len(self.heap) and self.heap[2*currIndex]<self.heap[currIndex]:
                self.heap[currIndex],self.heap[2*currIndex] = self.heap[2*currIndex], self.heap[currIndex]
                currIndex =2*currIndex
            else:
                break
        
    # we make evry subtree heap a legit heap
    def heapify(self,arr):
        arr.append(arr[0])
        currIndex = len(arr)//2

        while currIndex>0:
            if arr[currIndex]>arr[2*currIndex] or arr[currIndex]>arr[2*currIndex+1]:
                
        

    
               





            


         