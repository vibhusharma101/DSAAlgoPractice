# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# n=5
# +++++
#  +++
#   +

def practice(arr,n):
    bdth = n
    while n>0:
        stIndex = (bdth-n)//2
        enIndex = bdth -stIndex
        for index in range(bdth):
            if index>=stIndex and index<enIndex:
                print("+",end="")
            else:
                print(" ",end="")
        print("")
        n= n-2
    return ""

def practiceSecondIteration(arr,n):
    bdth = n
    leadingSpaces = 0
    while n>0:
        for index in range(leadingSpaces):
            print(" ",end="")
        for index in range(n):
            print("+",end="")
        for index in range(leadingSpaces):
            print(" ",end="")
        print("")
        n= n-2
        leadingSpaces = leadingSpaces+2
    return ""

practice([],5)
practiceSecondIteration([],3)

## Learn How Authentication Works and all.