#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 749. 约翰的后花园,题目地址：https://www.lintcode.com/problem/johns-backyard-garden/description
# 约翰想在他家后面的空地上建一个后花园，现在有两种砖，一种3 dm的高度，7 dm的高度。约翰想围成x dm的墙。如果约翰能做到，输出YES，否则输出NO。
#  X是一个整数，取值范围为 [3, 1000]。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isBuild(10)
        expect = "YES"
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isBuild(5)
        expect = "NO"
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isBuild(13)
        expect = "YES"
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.isBuild(3)
        expect = "YES"
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        res = "NO"
        for i in range(x // 7 + 1):
            if (x - i * 7) % 3 == 0:
                res = "YES"
                break
        return res


if __name__ == '__main__':
    unittest.main()

