# Search a 2D Matrix
# Solved 
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

class Solution:

    def searchMatrixBrute(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force ( O(m log n))
        for index in range(len(matrix)):
            print(len(matrix[0]),index)
            startIndex = 0 
            endIndex = len(matrix[0])-1
            while startIndex<=endIndex:
                mid  = (startIndex+endIndex)//2
                if matrix[index][mid] ==target:
                    return True
                elif matrix[index][mid] <target:
                    startIndex = mid+1
                else:
                    endIndex = mid-1    
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Better approach ( O( log (n*m)))

        startIndex = 0
        endIndex = (len(matrix)*len(matrix[0]))-1

        while startIndex<=endIndex:
            mid = (startIndex+endIndex)//2
            rowIndex = mid//len(matrix[0])
            columnIndex = mid%len(matrix[0])

            if matrix[rowIndex][columnIndex] == target:
                return True
            elif matrix[rowIndex][columnIndex]>target:
                endIndex = mid-1
            else:
                startIndex = mid+1
        
        return False




