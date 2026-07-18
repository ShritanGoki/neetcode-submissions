# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur):
            if not cur:
                return [True, 0]

            left = dfs(cur.left)
            right = dfs(cur.right)
            difference = abs(left[1]-right[1])

            balance = left[0] and right[0] and difference <=1
            return [balance, 1 + max(left[1], right[1])]

        res = dfs(root)
        return res[0]






            
