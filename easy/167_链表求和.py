#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 167.链表求和,题目地址：https://www.lintcode.com/problem/add-two-numbers/description
# 你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_one_none(self):
        l1 = makeLinkedList(None)
        l2 = makeLinkedList([5,9,2])
        result = self.solutionCase.addLists(l1, l2)
        expect = makeLinkedList([5,9,2])
        self.assertEqual(result.val, expect.val)
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.next.next.val, expect.next.next.val)
        self.assertEqual(result.next.next.next, expect.next.next.next)
        
    def test_carry(self):
        l3 = makeLinkedList([1,1,8])
        l4 = makeLinkedList([5,6,2])
        result = self.solutionCase.addLists(l3, l4)
        expect = makeLinkedList([6,7,0,1])
        self.assertEqual(result.val, expect.val)
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.next.next.val, expect.next.next.val)
        self.assertEqual(result.next.next.next.val, expect.next.next.next.val)
        
    def test_two_lists(self):
        l5 = makeLinkedList([3,1,5])
        l6 = makeLinkedList([5,9,2])
        result = self.solutionCase.addLists(l5, l6)
        expect = makeLinkedList([8,0,8])
        self.assertEqual(result.val, expect.val)
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.next.next.val, expect.next.next.val)
        self.assertEqual(result.next.next.next, expect.next.next.next)
        
        
def makeLinkedList(l):
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
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        headNode = None
        if l1 or l2:
            if l1 is None:
                sum = l2.val
                l2 = l2.next
            elif l2 is None:
                sum = l1.val
                l1 = l1.next
            else:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            headNode = ListNode(sum)
            nextNode = headNode
        while l1 or l2:
            if l1 is None:
                sum = l2.val
                l2 = l2.next
            elif l2 is None:
                sum = l1.val
                l1 = l1.next
            else:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            nextNode.next = ListNode(sum)
            nextNode = nextNode.next
        carryNode = headNode
        while carryNode:
            if carryNode.val >= 10:
                carryNode.val -= 10
                if carryNode.next:
                    carryNode.next.val += 1
                else:
                    carryNode.next = ListNode(1)
            carryNode = carryNode.next
        return headNode

        
if __name__ == '__main__':
    unittest.main()
