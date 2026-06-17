# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            ret.append(node.val)
            cur = node.right
        return ret

    """
    Recursive way
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.inorder(root, ret)
        return ret
         
    def inorder(self, root: Optional[TreeNode], arr: List[int]) -> None:
        if not root:
            return 
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    """
         
        