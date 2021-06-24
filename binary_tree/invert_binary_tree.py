"""
翻转二叉树
https://leetcode-cn.com/problems/invert-binary-tree/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        注意判断边界值，
        在子节点递归调用翻转函数        
        """
        if root == None:
            return root
        tmp = root.left 
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root