"""
填充每个节点的下一个右侧节点
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    注意对比与226 翻转二叉树的区别，这里的递归函数中传入了两个参数（两个节点）
    """
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        self.connectTwoNode(root.left, root.right)

        return root
    
    def connectTwoNode(self, left, right):
        # 编辑判断要放在这里做，在connect中做没有用，因为递归调用的是这个函数
        if left == None or right == None:
            return None
        left.next = right
        self.connectTwoNode(left.left, left.right)
        self.connectTwoNode(left.right, right.left)
        self.connectTwoNode(right.left, right.right)