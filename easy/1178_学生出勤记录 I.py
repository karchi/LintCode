#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1178. 学生出勤记录 I,题目地址：https://www.lintcode.com/problem/student-attendance-record-i/description
# 给定一个字符串表示学生出勤记录，记录仅由下列三个字符组成：
# 'A' : 缺席（Absent）.
# 'L' : 迟到（Late）.
# 'P' : 到场（Present）.
# 如果学生的出勤情况不包含 超过一个'A'(缺席) 或者 超过连续两个'L'(迟到) ，那么他就应该受到奖励。
# 返回该学生是否会受到奖励。
# 样例:
# 样例 1:输入: "PPALLP",输出: True
# 样例 2:输入: "PPALLL",输出: False
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.checkRecord("PPALLP")
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.checkRecord("PPALLL")
        expect =  False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.checkRecord("PPLLL")
        expect = False
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.checkRecord("PPALALP")
        expect = False
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """
    def checkRecord(self, s):
        return s.count("A")<2 and s.count("LLL")==0


if __name__ == '__main__':
    unittest.main()
