#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 372. Delete Node in a Linked List,题目地址：https://www.lintcode.com/problem/delete-node-in-a-linked-list/description
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.linkedList = makeLinkedList([1,2,3,4])
        self.solutionCase = Solution()
        
    def test_del_3(self):
        self.solutionCase.deleteNode(self.linkedList.next.next)
        self.assertEqual(self.linkedList.val, 1)
        self.assertEqual(self.linkedList.next.val, 2)
        self.assertEqual(self.linkedList.next.next.val, 4)


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


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

        
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        

if __name__ == '__main__':
    unittest.main()
