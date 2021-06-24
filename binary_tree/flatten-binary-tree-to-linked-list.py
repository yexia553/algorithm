"""
把二叉树拉直变为一个链表
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        self.flatten(root.right)
        self.flatten(root.left)
        right = root.right
        left = root.left

        root.left = None
        root.right = left

        p = root
        while p.right != None:
            p = p.right
        
        p.right = right