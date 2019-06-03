#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 174. 删除链表中倒数第n个节点，题目地址：https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/description
# 给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
# 链表中的节点个数大于等于n
# 样例:
# 样例 1:Input: list = 1->2->3->4->5->null， n = 2;	Output: 1->2->3->5->null
# 样例 2:Input:  list = 5->4->3->2->1->null, n = 2;	Output: 5->4->3->1->null
# 挑战：O(n)时间复杂度
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.removeNthFromEnd(makeLinkedList([1,2,3,4,5]), 2)
        expect = makeLinkedList([1,2,3,5])
        self.assertEqual(result.next.next.next.val, expect.next.next.next.val)
        
    def test_1(self):
        result = self.solutionCase.removeNthFromEnd(makeLinkedList([1,2,3,4,5]), 5)
        expect = makeLinkedList([2,3,4,5])
        self.assertEqual(result.val, expect.val)
        
        
# 定义链表
def makeLinkedList(l):
    # @param l: a list like [1,0,1,9]
    # @return: the headNode of l
    headNode = None
    if l:
        headNode = ListNode(l.pop(0))
        nextNode = headNode
    while l:
        nextNode.next = ListNode(l.pop(0))
        nextNode = nextNode.next
    return headNode
    
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
     

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        while n:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if fast:
            slow.next = slow.next.next
        else:
            head = head.next
        return head


if __name__ == '__main__':
    unittest.main()
