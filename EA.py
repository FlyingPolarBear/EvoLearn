'''
Author: Derry
Date: 2022-09-23 14:49:09
LastEditors: Derry
Email: drlv@mail.ustc.edu.cn
LastEditTime: 2022-10-12 23:19:55
Description: Evolutionary Learning （演化学习算法）
'''
import numpy as np

from UBoolean import UBoolean


class EvoLearn:
    """
    演化算法是一类通用的启发式优化算法
    """

    def __init__(self, f=lambda x: np.sum(x)):
        self.f = f

    def _bit_wise_mutation(self, s):
        """
        逐位变异算子
        """
        s_new = s.copy()
        p = 1/s.shape[0]
        mask = np.random.rand(*s.shape) < p
        s_new[mask] = 1 - s[mask]
        return s_new

    def _one_bit_mutation(self, s):
        """
        一位变异算子
        """
        s_new = s.copy()
        i = np.random.randint(0, s.shape[0])
        s_new[i] = 1 - s[i]
        return s_new

    def Alg_1_1_EA(self, n=10, iter=100, strict=False, RLS=False):
        """
        (1+1)-EA 算法 & RLS 算法

        parameters:
            n: the length of the bit string
            iter: the number of iterations
            strict: the selection mechanism （严格选择机制）
            RLS: Randomized Local Search （随机局部搜索）
        """
        print(
            f"Alg:{'(1+1)-EA' if not RLS else 'RLS'}{'≠' if strict else ''} on Func: {self.f.__name__}")
        s = np.random.randint(0, 2, n)
        for i in range(iter):
            s_new = self._bit_wise_mutation(
                s) if RLS else self._one_bit_mutation(s)
            if self.f(s_new) > self.f(s) or (self.f(s_new) == self.f(s) and not strict):
                s = s_new
            print(
                f"iter:{i:4d}  s: {''.join(map(str,map(int,s)))}  f_value: {self.f(s):.2f}")
        return s

    def Alg_mu_1_EA(self, n=10, iter=100, mu=10):
        """
        (μ+1)-EA 算法

        parameters:
            n: the length of the bit string
            iter: the number of iterations
            μ: the number of parents （父代种群规模）
        """
        print(f"Alg:({mu}+1)-EA on Func: {self.f.__name__}")
        P = np.random.randint(0, 2, (mu, n))
        for i in range(iter):
            s = P[np.random.randint(0, mu)]
            s_new = self._one_bit_mutation(s)
            FP = np.array([self.f(z) for z in P])
            z_index = np.argmax(FP)
            if self.f(s_new) > FP[z_index]:
                P[z_index] = s_new
            print(
                f"iter:{i:4d}  s: {''.join(map(str,map(int,s)))}  f_value: {self.f(s):.2f}")
        return P

    def Alg_1_lambda_EA(self, n=10, iter=100, lambda_=10):
        """
        (1+λ)-EA 算法

        parameters:
            n: the length of the bit string
            iter: the number of iterations
            λ: the number of children （子代种群规模）
        """
        print(f"Alg:(1+{lambda_})-EA on Func: {self.f.__name__}")
        s = np.random.randint(0, 2, n)
        for i in range(iter):
            s_new = np.zeros((lambda_, n))
            for j in range(lambda_):
                s_new[j] = self._one_bit_mutation(s)
            s_new_max = s_new[np.argmax([self.f(ss) for ss in s_new])]
            if self.f(s_new_max) > self.f(s):
                s = s_new_max
            print(
                f"iter:{i:4d}  s: {''.join(map(str,map(int,s)))}  f_value: {self.f(s):.2f}")
        return s

    def Alg_mu_lambda_EA(self, n=10, iter=100, mu=10, lambda_=10):
        """
        (μ+λ)-EA 算法

        parameters:
            n: the length of the bit string
            iter: the number of iterations
            μ: the number of parents （父代种群规模）
            λ: the number of children （子代种群规模）
        """
        print(f"Alg:({mu}+{lambda_})-EA on Func: {self.f.__name__}")
        P = np.random.randint(0, 2, (mu, n))
        for i in range(iter):
            s_new = np.zeros((lambda_, n))
            for j in range(lambda_):
                s = P[np.random.randint(0, mu)]
                s_new[j] = self._one_bit_mutation(s)
            ans_set = np.concatenate((P, s_new))
            ans_set = ans_set[np.argsort(
                [self.f(ss) for ss in ans_set])]  # 按照f值排序
            P = ans_set[-mu:]
            print(
                f"iter:{i:4d}  s: {''.join(map(str,map(int,s)))}  f_value: {self.f(s):.2f}")
        return P

    def Alg_SEMO(self, n=10, iter=100, global_=False):
        """
        SEMO: simple evolutionary multi-objective optimizer （简单演化多目标优化法）

        parameters:
            n: the length of the bit string
            iter: the number of iterations
            global_: search globally （全局搜索）
        """
        print(f"Alg:{'GSEMO' if global_ else 'SEMO'} on Func:{self.f.__name__}")
        s = np.random.randint(0, 2, n)
        P = np.array([s])
        for i in range(iter):
            s = P[np.random.randint(0, P.shape[0])]
            if global_:  # global search（全局搜索）
                s_new = self._bit_wise_mutation(s)
            else:  # local search（局部搜索）
                s_new = self._one_bit_mutation(s)
            FP = np.array([self.f(z) for z in P])
            if self.f(s_new) > max(FP):
                P = P[FP < self.f(s_new)]
                P = np.concatenate((P, np.array([s_new])))
            print(
                f"iter:{i:4d}  s: {''.join(map(str,map(int,s)))}  f_value: {self.f(s):.2f}")
        return s


def test_EA(n=10, iter=100):
    """
    测试演化算法
    """
    evo = EvoLearn()
    ub = UBoolean()
    for f in [ub.OneMax, ub.LeadingOnes, ub.Peaks, ub.Trap, ub.LOLZ, ub.COCZ]:
        evo.f = f
        evo.Alg_1_1_EA(n=n, iter=iter)  # (1+1)-EA
        evo.Alg_1_1_EA(n=n, iter=iter, strict=True)  # (1+1)-EA≠
        evo.Alg_1_1_EA(n=n, iter=iter, RLS=True)  # RLS
        evo.Alg_1_1_EA(n=n, iter=iter, strict=True, RLS=True)  # RLS≠
        evo.Alg_mu_1_EA(n=n, iter=iter, mu=10)  # (μ+1)-EA
        evo.Alg_1_lambda_EA(n=n, iter=iter, lambda_=10)  # (1+λ)-EA
        evo.Alg_mu_lambda_EA(n=n, iter=iter, lambda_=10, mu=10)  # (μ+λ)-EA
        evo.Alg_SEMO(n=n, iter=iter)  # SEMO
        evo.Alg_SEMO(n=n, iter=iter, global_=True)  # GSEMO


if __name__ == "__main__":
    test_EA()
