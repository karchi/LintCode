#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 632. 二叉树的最大节点,题目地址：https://www.lintcode.com/problem/binary-tree-maximum-node/description
# 在二叉树中寻找值最大的节点并返回。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()

    def test_none(self):
        tree2 = makeBinaryTree([])
        result = self.solutionCase.maxNode(tree2)
        self.assertEqual(result, None)
    
    def test_1(self):
        tree1 = makeBinaryTree([1])
        result = self.solutionCase.maxNode(tree1)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left, None)
        
    def test_5(self):
        tree5 = makeBinaryTree([1, -5, 2, None, None, -4, -5])
        result = self.solutionCase.maxNode(tree5)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.left.val, -4)
        self.assertEqual(result.right.val, -5)
        
    def test_7(self):
        tree7 = makeBinaryTree([1, -5, 2, 0, 3, -4, -5])
        result = self.solutionCase.maxNode(tree7)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left, None)


def makeBinaryTree(tree_list):
    # @param tree_list: a list like [1,0,None,9]
    # @return: the root of tree_list
    root = None
    if tree_list:
        root = TreeNode(tree_list.pop(0))
        nodeQuere = [root]
    if len(tree_list) % 2:
        tree_list.append(None)
    while tree_list:
        nextNode = nodeQuere.pop(0)
        if tree_list[0]:
            nextNode.left = TreeNode(tree_list.pop(0))
            nodeQuere.append(nextNode.left)
        else:
            tree_list.pop(0)
        if tree_list[0]:
            nextNode.right = TreeNode(tree_list.pop(0))
            nodeQuere.append(nextNode.right)
        else:
            tree_list.pop(0)   
    return root
        

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root:
            if root.left != None or root.right != None:
                left_max = Solution.maxNode(self, root.left)
                right_max = Solution.maxNode(self, root.right)
                if left_max != None and left_max.val > root.val:
                    root = left_max
                if right_max != None and right_max.val > root.val:
                    root = right_max
        return root


if __name__ == '__main__':
    unittest.main()

