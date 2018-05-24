#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 452. 删除链表中的元素,题目地址：https://www.lintcode.com/problem/remove-linked-list-elements/description
# 删除链表中等于给定值val的所有节点。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution_case = Solution()
        
    def test_linded_list(self):
        linked_list = makeLinkedList([1,2,3,4,5,3])
        self.assertEqual(self.solution_case.removeElements(linked_list, 3).next.next.val, 4)
        self.assertEqual(self.solution_case.removeElements(linked_list, 3).next.next.next.next, None)
        
    def test_none(self):
        self.assertEqual(self.solution_case.removeElements(None, 2), None)
        
    def test_one_element(self):
        linked_list = makeLinkedList([3])
        self.assertEqual(self.solution_case.removeElements(linked_list, 2).next, None)
        self.assertEqual(self.solution_case.removeElements(linked_list, 2).val, 3)
        
    def test_del_headnode(self):
        linked_list = makeLinkedList([1,2,3,1,2,3])
        self.assertEqual(self.solution_case.removeElements(linked_list, 1).val, 2)
        self.assertEqual(self.solution_case.removeElements(linked_list, 1).next.val, 3)
        self.assertEqual(self.solution_case.removeElements(linked_list, 1).next.next.val, 2)

        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        thisNode = head
        while thisNode:
            while thisNode.next and thisNode.next.val == val:
                thisNode.next = thisNode.next.next
            thisNode = thisNode.next
        return head
 

if __name__ == '__main__':
    unittest.main()


