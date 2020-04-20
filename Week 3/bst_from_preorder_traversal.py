from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# First Attempt: Wrong Answer
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        cursor = root
        for num in preorder[1:]:
            if num < cursor.val:
                self.addToLeft(cursor, num)
            else:
                while (cursor.right):
                    cursor = cursor.parent
                self.addToRight(cursor, num)


    def addToLeft(self, node: TreeNode, value: int):
        new_node = self.createNode(node, value)
        node.left = new_node

    def addToRight(self, node: TreeNode, value: int):
        new_node = self.createNode(node, value)
        node.right = new_node

    def createNode(self, node: TreeNode, value: int) -> TreeNode:
        new_node = TreeNode(value)
        new_node.parent = node
        return new_node


##################################################################


# Second Attempt: Accepted
def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    stack = [root]
    for num in preorder[1:]:
        if num < stack[-1].val:
            stack[-1].left = TreeNode(num)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < num:
                last = stack.pop()
            last.right = TreeNode(num)
            stack.append(last.right)
    return root


# The tracking cursor failed to keep track of nested
# values, so replacing it with a stack did the job