# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        self.recursiveMaxPathSum(root)
        return self.maximum

    def recursiveMaxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        left = max(self.recursiveMaxPathSum(root.left), 0)
        right = max(self.recursiveMaxPathSum(root.right), 0)
        
        curr_max = left + right + root.val
        self.maximum = max(self.maximum, curr_max)
        
        return max(left, right) + root.val


# For every node, the maximum path can either be:
#   - root.val
#   - root.val + leftPath
#   - root.val + rightPath
#   - root.val + leftPath + rightPath