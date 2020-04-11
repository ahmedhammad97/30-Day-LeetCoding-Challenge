# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.computeDiameter(root)
        return self.diameter
    
    def computeDiameter(self, root):
        if not root: return 0
        
        leftDiameter = self.computeDiameter(root.left)
        rightDiameter = self.computeDiameter(root.right)
        currDiameter = leftDiameter + rightDiameter
        
        self.diameter = max(self.diameter, currDiameter)
        return 1 + max(leftDiameter, rightDiameter)


# There is an obvious recurrence here, where the diameter
# at every node, is the sum of the longest left path, and
# the longest right path.

# Since the longest diameter is not necessarily the one at
# the root, the longest diameter should be checked at every
# node, and compared with a class field.