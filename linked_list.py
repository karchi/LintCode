#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
