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

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next =  None
            
        
        return newHead     

