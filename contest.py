import sys

# It's recommended to increase the recursion limit for problems involving deep recursion.
# sys.setrecursionlimit(10**6)

# Fast I/O functions
# These read from the input buffer and are much faster than the standard input().
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def S(): return sys.stdin.readline().strip()
def LS(): return sys.stdin.readline().split()

# ------------------------------------------------------------------------------------ #

def solve():
    """
    This is where you write the core logic for a single test case.
    """
    # Example: Read two numbers and an array
    n,k = LI()
    arr = S()

    ans = list('+'*n)
    lp =0
    rp = n-1

    for i in range(len(arr)):
        if arr[i]=='0':
            if lp>0 and ans[lp-1]=='?':
                ans[lp]='?'
                ans[lp-1]='-'
            else:
                ans[lp]='-'
            lp+=1
        elif arr[i]=='1':
            if rp+1<len(ans) and ans[rp+1]=='?':
                ans[rp+1]='-'
                ans[rp]='?'
            else:
                ans[rp] ='-'
            rp-=1
        else:
            ans[lp]='?'
            ans[rp]='?'
            if len(ans)==1:
                ans[0]='-'
            lp+=1
            rp-=1



    print(''.join(ans))

    
    
# ------------------------------------------------------------------------------------ #

# This is the main execution block.
if __name__ == "__main__":
    # Read the number of test cases.
    # Most contests have a 't' that specifies how many times to run the solve() function.
    try:
        t = I()
        for _ in range(t):
            solve()
    except (IOError, EOFError):
        solve()