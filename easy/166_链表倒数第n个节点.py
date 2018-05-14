#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 166.链表倒数第n个节点 ,题目地址：https://www.lintcode.com/problem/nth-to-last-node-in-list/description
# 找到单链表倒数第n个节点，保证链表中节点的最少数量为n。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.listNode11 = ListNode(3)
        self.listNode12 = ListNode(2)
        self.listNode13 = ListNode(1)
        self.listNode14 = ListNode(5)
        self.listNode11.next = self.listNode12
        self.listNode12.next = self.listNode13
        self.listNode13.next = self.listNode14
        self.solutionCase = Solution()
        
    def test1(self):
        expect = 1
        result = self.solutionCase.nthToLast(self.listNode11, 2).val
        self.assertEqual(result, expect)
        
    def test2(self):
        expect = 5
        result = self.solutionCase.nthToLast(self.listNode11, 1).val
        self.assertEqual(result, expect)
        
    def test3(self):
        expect = 3
        result = self.solutionCase.nthToLast(self.listNode11, 4).val
        self.assertEqual(result, expect)


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


'''
# Solution 1:
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        lenth = 0
        thisNode = head
        while thisNode:
            lenth += 1
            thisNode = thisNode.next
        n = lenth - n
        thisNode = head
        while n > 0:
            n -= 1
            thisNode = thisNode.next
        return thisNode
'''


# Solution 2:
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        fastNode = slowNode = head
        while n:
            fastNode = fastNode.next
            n -= 1
        while fastNode:
            slowNode = slowNode.next
            fastNode = fastNode.next
        return slowNode

    
if __name__ == '__main__':
    unittest.main()


