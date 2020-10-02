"""
94. Binary Tree Inorder Traversal
# Definition for a binary tree node.

Recursively:
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal_1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        root.visited = True
        while stack:
            cur = stack[-1]
            while cur:
                if cur.left and not hasattr(cur.left, "visited"):
                    cur.left.visited = True
                    stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
        return res

    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
            