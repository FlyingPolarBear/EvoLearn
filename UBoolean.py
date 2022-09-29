'''
Author: Derry
Date: 2022-09-29 17:00:37
LastEditors: Derry
Email: drlv@mail.ustc.edu.cn
LastEditTime: 2022-09-29 17:05:21
Description: UBoolean函数类
'''
import numpy as np


class UBoolean:
    """
    UBoolean函数类由一大类非平凡的伪布尔函数构成，
    其中每个函数的全局最优解都是唯一的
    """

    def __init__(self):
        pass

    def OneMax(self, s):
        """
        OneMax问题：

        最大化一个解中1-位的个数

        最优值：1^n
        """
        return np.sum(s)

    def LeadingOnes(self, s):
        """
        LeadingOnes问题：

        最大化一个解中从首端开始连续1-位的数目

        最优值：1^n
        """
        for i in range(len(s)):
            if s[i] == 0:
                return i
        return len(s)

    def Peaks(self, s):
        """
        Peaks问题：

        在除最优解1^n以外的所有解上具有相同的相似度

        最优值：0
        """
        return np.prod(s)

    def Trap(self, s):
        """
        Trap问题：

        在最优解1^n之外，最大化一个解中0-位的数目

        最优值：c - n > 0
        """
        c = len(s)+1
        return c*np.prod(s) - np.sum(s)

    def LOLZ(self, s, alpha=0.5):
        """
        LOLZ问题：

        目标一：最大化从解的首端开始的连续的1-位的数目（LeadingOnes）
        目标二：最大化从解的尾端开始的连续的0-位的数目

        帕累托最优解：0^n, 10^(n-1), ..., 1^n
        """
        return alpha*self.LeadingOnes(s) + (1-alpha)*self.LeadingOnes(1-s[::-1])

    def COCZ(self, s, alpha=0.5):
        """
        COCZ问题：

        目标一：最大化解中1-位的数目（OneMax）
        目标二：最大化解前半部分中1-位的数目和后半部分中0-位的数目之和

        帕累托最优解集合：{1^(n/2)*^(n/2)|*∈{0,1}}
        """
        return alpha*self.OneMax(s) + (1-alpha)*(self.OneMax(s[:len(s)//2+1])+self.OneMax(1-s[len(s)//2+1:]))

