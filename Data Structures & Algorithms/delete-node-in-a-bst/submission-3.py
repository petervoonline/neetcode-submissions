# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        par = None
        cur = root
        while cur and cur.val != key:
            par = cur
            if key < cur.val:
                cur = cur.left
            elif key > cur.val:
                cur = cur.right
        
        # key not in bst
        if not cur:
            return root
            
        #Node with one child or zero child
        if (not cur.left) or (not cur.right):  # if one is empty, this will be true
            # child can be None or either left or right
            child = cur.left
            if not child:
                child = cur.right
            # key is root
            if not par:
                return child
            
            if cur.val > par.val:
                par.right = child
            else:
                par.left = child
        
        # Node with two child
        else:
            '''
            - find the minimum value on the right
                + assign the current cu to another var to keep track cause we will move cur to find min
                + from cur, go right once
                (has to exist since cur is node to be deleted and has two children)
                + while loop to find the min value by keep going left until cur.left is none
                + also have to keep track of node to be deleted, the min value (cur), and parent of min

            2. identify the if root or not
            2. 
            '''
            toBeDelNode = cur
            minPar = None
            cur = cur.right 

            while cur.left:
                minPar = cur
                cur = cur.left
            
            if minPar:
                minPar.left = cur.right
                cur.right = toBeDelNode.right

            cur.left = toBeDelNode.left
            

            if not par:
                return cur
             
            if cur.val > par.val:
                par.right = cur
            else:
                par.left = cur
            
        return root
