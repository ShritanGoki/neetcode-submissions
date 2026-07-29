# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        
        def dfs(node):
            nonlocal maxSum

            if node == None:
                return 0
            
            maxLeft = max(dfs(node.left), 0)
            maxRight = max(dfs(node.right), 0)

            maxSum = max(node.val + maxLeft + maxRight, maxSum)
            
            return node.val + max(maxLeft, maxRight)
        
        dfs(root)
        return maxSum
                

