#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 96. 链表划分，题目地址：https://www.lintcode.com/problem/partition-list/description
# 给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。你应该保留两部分内链表节点原有的相对顺序。
# 样例:
# 样例 1:输入: list = null, x = 0.输出: null.样例解释:空链表本身满足要求
# 样例 2:输入: list = 1->4->3->2->5->2->null, x = 3.输出: 1->2->2->4->3->5->null.样例解释:要保持原有的相对顺序。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.partition(makeLinkedList(None),0)
        expect = None
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.partition(makeLinkedList([1,4,3,2,5,2]),3)
        expect =  makeLinkedList([1,2,2,4,3,5])
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.next.next.next.val, expect.next.next.next.val)
        
        
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
    def __init__(self, x, next=None):
        self.val = x
        self.next = next        
        
        
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        left_head = None
        right_head = None
        left_tail = None
        right_tail = None
        while head:
            if head.val < x:
                if left_tail:
                    left_tail.next = ListNode(head.val)
                    left_tail = left_tail.next
                else:
                    left_head = ListNode(head.val)
                    left_tail = left_head
            else:
                if right_tail:
                    right_tail.next = ListNode(head.val)
                    right_tail = right_tail.next
                else:
                    right_head = ListNode(head.val)
                    right_tail = right_head
            head = head.next
        if left_head:
            left_tail.next = right_head
            return left_head
        else:
            return right_head


if __name__ == '__main__':
    unittest.main()