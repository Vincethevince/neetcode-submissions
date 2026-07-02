# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
    
        def maxD(root):
            nonlocal res 
            if not root:
                return 0
            
            #return 1+ max(self.maxD(root.left),self.maxD(root.left))
            left = maxD(root.left)
            right = maxD(root.right)
            res = max(res, left+right)

            return  1 + max(left, right)

        maxD(root)
        return res


        