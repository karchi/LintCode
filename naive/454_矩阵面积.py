#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 454. 矩阵面积,题目地址：http://www.lintcode.com/problem/rectangle-area/description
# 实现一个矩阵类Rectangle，包含如下的一些成员变量与函数：
# 两个共有的成员变量 width 和 height 分别代表宽度和高度。
# 一个构造函数，接受2个参数 width 和 height 来设定矩阵的宽度和高度。
# 一个成员函数 getArea，返回这个矩阵的面积。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_3_4(self):
        rec = Rectangle(3, 4)
        result = rec.getArea()
        expect = 12
        self.assertEqual(result, expect)
        
    def test_0_0(self):
        rec = Rectangle(0, 0)
        result = rec.getArea()
        expect = 0
        self.assertEqual(result, expect)


class Rectangle:
    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    def getArea(self):
        return self.width * self.height


if __name__ == '__main__':
    unittest.main()

