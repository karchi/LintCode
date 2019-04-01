#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 112. 删除排序链表中的重复元素，题目地址：https://www.lintcode.com/problem/remove-duplicates-from-sorted-list/description
# 给定一个排序链表，删除所有重复的元素每个元素只留下一个。
# 样例:
# 样例 1:输入:  null,输出: null
# 样例 2:输入: 1->1->2->null,输出: 1->2->null
# 样例 3:输入: 1->1->2->3->3->null,输出: 1->2->3->null
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.deleteDuplicates(None)
        expect = None
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.deleteDuplicates(makeLinkedList([1,1,2]))
        expect = makeLinkedList([1,2])
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.val, expect.val)
        
    def test_2(self):
        result = self.solutionCase.deleteDuplicates(makeLinkedList([1,1,2,3,3]))
        expect = makeLinkedList([1,2,3])
        self.assertEqual(result.next.val, expect.next.val)
        self.assertEqual(result.val, expect.val)
        
    def test_3(self):
        result = self.solutionCase.deleteDuplicates(makeLinkedList([1]))
        expect = makeLinkedList([1])
        self.assertEqual(result.val, expect.val)

        
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
        
        
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        if head:
            tail = head
            while tail.next:
                if tail.val == tail.next.val:
                    tail.next = tail.next.next
                else:
                    tail = tail.next
        return head


if __name__ == '__main__':
    unittest.main()
