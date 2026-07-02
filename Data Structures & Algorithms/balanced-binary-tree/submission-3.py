# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # balanced, height
            if not root:
                return [True,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            h = 1 + max(left[1], right[1])
            if not left[0] or not right[0]:
                return [False, h]
            
            elif abs(left[1] - right[1]) > 1:
                return [False, h]
            return [True,h]
        
        return dfs(root)[0]
