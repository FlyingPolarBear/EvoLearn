# 演化学习 Evolutionary Learning

## 演化学习算法

1. $(1+1)-EA$
   ```python
   EvoLearn.Alg_1_1_EA(n=n, iter=iter)
   ```
2. $(1+1)-EA^{\neq}$
   ```python
   EvoLearn.Alg_1_1_EA(n=n, iter=iter, strict=True)
   ```
3. $RLS$
   ```python
   EvoLearn.Alg_1_1_EA(n=n, iter=iter, RLS=True)
   ```
4. $RLS^{\neq}$
   ```python
   EvoLearn.Alg_1_1_EA(n=n, iter=iter, strict=True, RLS=True)
   ```
5. $(\mu+1)-EA$
   ```python
   EvoLearn.Alg_mu_1_EA(n=n, iter=iter, mu=10)
   ```
6. $(1+\lambda)-EA$
   ```python
   EvoLearn.Alg_1_lambda_EA(n=n, iter=iter, lambda_=10)
   ```
7. $(\mu+\lambda)-EA$
   ```python
   EvoLearn.Alg_mu_lambda_EA(n=n, iter=iter, lambda_=10, mu=10)
   ```
8. $SEMO$
   ```python
   EvoLearn.Alg_SEMO(n=n, iter=iter) 
   ```
9. $GSEMO$
   ```python
   EvoLearn.Alg_SEMO(n=n, iter=iter, global_=True) 
   ```

## UBoolean函数类
1. OneMax问题
2. LeadingOnes问题
3. Peak问题
4. Trap问题
5. LOTZ问题
6. COCZ问题


