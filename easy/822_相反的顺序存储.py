#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 822. 相反的顺序存储,题目地址：https://www.lintcode.com/problem/reverse-order-storage/description
# 给出一个链表，并将链表的值以倒序存储到数组中。
# 您不能改变原始链表的结构。
# ListNode 有两个成员变量：ListNode.val 和 ListNode.next
# 样例:
# 样例1：输入: 1 -> 2 -> 3 -> null。输出: [3,2,1]
# 样例2：输入: 4 -> 2 -> 1 -> null。输出: [1,2,4]
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.reverseStore(makeLinkedList([1,2,3]))
        expect = [3,2,1]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.reverseStore(makeLinkedList([4,2,1]))
        expect =  [1,2,4]
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.reverseStore(makeLinkedList([]))
        expect = []
        self.assertEqual(result, expect)
        

'''
# 定义链表
'''
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

# 解法一：
class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        res = []
        while(head):
            res.insert(0, head.val)
            head = head.next
        return res


if __name__ == '__main__':
    unittest.main()
