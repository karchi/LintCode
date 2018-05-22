#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 375. 克隆二叉树 ,题目地址：https://www.lintcode.com/problem/clone-binary-tree/description
# 深度复制一个二叉树。
# 给定一个二叉树，返回一个他的 克隆品 。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution_case = Solution()
        
    def test1(self):
        tree1 = makeBinaryTree([1,2,3,4,5])
        self.assertEqual(self.solution_case.cloneTree(tree1).left.val, tree1.left.val)
        self.assertEqual(self.solution_case.cloneTree(tree1).val, tree1.val)
        self.assertEqual(self.solution_case.cloneTree(tree1).right.val, tree1.right.val)
        self.assertNotEqual(id(self.solution_case.cloneTree(tree1)), id(tree1))
        
    def test2(self):
        tree2 = makeBinaryTree([1,2,3,None,None,4,5])
        self.assertEqual(self.solution_case.cloneTree(tree2).left.left, tree2.left.left)
        self.assertEqual(self.solution_case.cloneTree(tree2).val, tree2.val)
        self.assertEqual(self.solution_case.cloneTree(tree2).right.left.val, tree2.right.left.val)
        self.assertNotEqual(id(self.solution_case.cloneTree(tree2)), id(tree2))
        
    def test_none(self):
        tree_none = makeBinaryTree([])
        self.assertEqual(self.solution_case.cloneTree(tree_none), tree_none)


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
        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        if root:
            treenode = TreeNode(root.val)
            treenode.left = Solution.cloneTree(self, root.left)
            treenode.right = Solution.cloneTree(self, root.right)
            return treenode
        else:
            return root

    
if __name__ == '__main__':
    unittest.main()

