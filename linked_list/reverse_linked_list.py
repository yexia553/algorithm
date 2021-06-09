"""
 92. 反转链表 II  https://leetcode-cn.com/problems/reverse-linked-list-ii/
反转链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def __init__(self):
        self.successor = ''

    def reverseList(self, head: ListNode) -> ListNode:
        '''
        反转整个连接
        '''
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseN(self, head: ListNode, n) -> ListNode:
        '''
        反转链表的前N个元素
        '''
        if n == 1:
            self.successor = head.next
            return head
        new_head = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return new_head

    def reverseBetween(self, head: ListNode, m, n) -> ListNode:
        '''
        反转链表的第M个到第N个元素， M < N
        '''
        if m == 1:
            return self.reverseN(head, n)
        # 进度迭代后返回的头结点是head.next，而不是head
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head