# In dp we usually save the results from previous calls
# so that we dont have do that again and again, it usually 
# is used in recursion problems
## this is 1D dp

# Brute Force ( TC 2^n)
def fibbonacci(n:int):
    if n<=1:
        return n
    return fibbonacci(n-1)+fibbonacci(n-2)


# Top Down DP ( starting at top of the tree and movong down )
# Some people donot consider it dp - it is basically using cachign and recursion
#TC - O(2n)
def fibonacciDP(n:int,cache)->int:
    if n<=1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacciDP[n-1]+fibonacciDP[n-2]
    return cache[n]

#TC - ( O(n))
#SC - O(n)
def fibonacciDPBottomUP(n:int):
    dp = [0,1]
    i = 2
    while i<=n:
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

# TC- O(n)
#SC - O(1)
def fibonacciDPBottomUPBetter(n:int):
    dp = [0,1]
    i =2
    while i<=n:
        dp[0],dp[1] = dp[1], dp[0]+dp[1]
    return dp[n]

print(fibonacciDP(5,{}))
print(fibonacciDPBottomUP(5))