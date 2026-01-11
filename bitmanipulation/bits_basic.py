

## Left bitwise is like dividing by 2 ( rounded off)
## right shift is like multiplying by 2
## count number of ones in represenation
def countBits(n):
    count  =0
    while n >0:
        if n&1==1:
            count+=1
        n = (n>>1)

    return count

# n&1 =1 in odd and n&1 = 0 in even case
# n|1 = 