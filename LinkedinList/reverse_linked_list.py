# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # First solution ( TC o(n))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curTail = None
        cur = head

        if cur != None:
            curNxt  = cur.next
            cur.next = curTail
            curTail  = cur
            cur  = curNxt
            
        while cur != None:
            curNxt = cur.next
            cur.next = curTail
            curTail  = cur
            cur = curNxt

        return curTail
    
    #Second Solution Cleaner (Recursion) ( TODO - undesratand the logic)

