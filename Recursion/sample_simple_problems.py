

class Solution:

    # Factorial Problem
    def findFactorial(self,n):
        if n <=1:
            return 1
        return n*self.findFactorial(n-1)
    
    #Fibonacci Problem ( TC - O(2^n))

    def findFibo(self, n):
        if n <=1:
            return 0
        if n ==2:
            return 1
        return self.findFibo(n-1)+ self.findFibo(self,n-2)
    
# Climbing Stairs Problem (  TC. ( O(2^n)))

# Climbing Stairs
# Solved 
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.


class Solution:
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n<=1:
            return 1 

        return self.climbStairs(n-1)+self.climbStairs(n-2)  

