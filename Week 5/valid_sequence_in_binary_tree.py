# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root: return len(arr) == 0
        if not arr: return False
        
        no_children = not root.left and not root.right
        if root.val != arr[0]: return False
        elif no_children and len(arr) == 1: return True
        
        left = self.isValidSequence(root.left, arr[1:])
        right = self.isValidSequence(root.right, arr[1:])
        return (len(arr) > 1) and (left or right)

# Come on, it's self-explanatory :D