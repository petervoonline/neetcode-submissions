# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret =  self.postOrder(root)
        return ret[0]


    def postOrder(self, root: Optional[TreeNode]) -> List[bool, int]:
        if not root:
            return [True, 0]
       
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        isBalanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

        return [isBalanced, 1 + max(left[1], right[1])]