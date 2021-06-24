"""
每K个一组反转单向链表
http://www.panzhixiang.cn/article/2021/6/21/25.html
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ## laluladong 解法(迭代)
    # def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
    #     pre = None
    #     cur = head
    #     nxt = head
    #     while cur != tail:
    #         nxt = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = nxt
    #     return pre

    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     if head == None:
    #         return head
    #     a = head
    #     b = head
    #     for item in range(k):
    #         if b != None:
    #             b = b.next
    #         else:
    #             return head
    #     newHead = self.reverse(a, b)
    #     a.next = self.reverseKGroup(b, k)
    #     return newHead

    ## 官方解法
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next  # 这里给prev赋值为None也可以，不影响结果，但是性能会差，为什么？
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:  # 这个循环会反转整个链表，替代了laluladong迭代解法中的递归调用
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail  # 此时的tail是后面一段子链表的hair（也就是pre）
            head = tail.next

        return hair.next