#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 35. 翻转链表，题目地址：https://www.lintcode.com/problem/reverse-linked-list/description
# 翻转一个链表
# 样例:
# 样例 1:输入: 1->2->3->null，输出: 3->2->1->null
# 样例 2:输入: 1->2->3->4->null，输出: 4->3->2->1->null
# 挑战：在原地一次翻转完成
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.reverse(makeLinkedList([1,2,3]))
        expect = makeLinkedList([3,2,1])
        self.assertEqual(result.val, expect.val)
    
    def test_1(self):
        result = self.solutionCase.reverse(makeLinkedList([1,2,3,4]))
        expect = makeLinkedList([4,3,2,1])
        self.assertEqual(result.next.val, expect.next.val)
        

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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head


if __name__ == '__main__':
    unittest.main()
