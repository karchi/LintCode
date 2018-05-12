#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 二叉树的最大深度,题目地址：https://www.lintcode.com/problem/maximum-depth-of-binary-tree/description
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.treenode1 = TreeNode(1)
        self.treenode2 = TreeNode(2)
        self.treenode3 = TreeNode(3)
        self.treenode4 = TreeNode(4)
        self.treenode5 = TreeNode(5)
        self.treenode1.left = self.treenode2
        self.treenode1.right = self.treenode3
        self.treenode3.left = self.treenode4
        self.treenode3.right = self.treenode5

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.maxDepth(self.treenode1), 3)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        res = 0
        if root:
            res += 1
            res += max(Solution.maxDepth(self, root.left), Solution.maxDepth(self, root.right))
        return res

    
if __name__ == '__main__':
    unittest.main()
