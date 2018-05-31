#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 3466. 链表节点计数,题目地址：https://www.lintcode.com/problem/count-linked-list-nodes/description
# 计算链表中有多少个节点.
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_3_nodes(self):
        A = makeLinkedList([1, 3, 5])
        result = self.solutionCase.countNodes(A)
        expect = 3
        self.assertEqual(result, expect)
        
    def test_none(self):
        A = makeLinkedList(None)
        result = self.solutionCase.countNodes(A)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1_node(self):
        A = makeLinkedList([2])
        result = self.solutionCase.countNodes(A)
        expect = 1
        self.assertEqual(result, expect)
    

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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        sum = 0
        while head:
            sum += 1
            head = head.next
        return sum


if __name__ == '__main__':
    unittest.main()

