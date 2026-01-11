
#Question

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Time complexity is O(log(n )) in searching in binary tree if the tree is roughly balanced ( it has almost equal number of left and right nodes)
# as in case of unbalanced search tree it will be more towards O(N) thing of tree with nodes 2,3,4 ( it will be O(n)) will go right every time)
# so usually the O( h ) where h is height of the tree it takes care of both the values.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans =[]
        curr = root
        while curr:
            if curr.val ==val:
                return curr
            elif curr.val >val:
                curr = curr.left
            else:
                curr = curr.right

        return None

    # using recursion 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans =[]
        curr = root
        if not root:
            return None
        
        if root.val==val:
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)