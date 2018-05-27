#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 定义二叉树
'''

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