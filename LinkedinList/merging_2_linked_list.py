# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode(0,None)
        curr =dummyNode

        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2  = list2.next
            curr = curr.next
        
        curr.next = list1 or list2

        return dummyNode.next 
    

#Recursion Solution 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0,None)
        if list1 and list2:
            if list1.val<list2.val:
                dummy.next = list1 
                dummy.next.next = self.mergeTwoLists(dummy.next.next,list2)
            else:
                dummy.next = list2
                dummy.next.next = self.mergeTwoLists(list1, dummy.next.next)
        else:
            dummy.next = list1 or list2
            
        
        return dummy.next