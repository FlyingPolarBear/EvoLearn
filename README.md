# Evolutionary Learning 演化学习

## 演化学习算法

#### (1+1)-EA
```python
EvoLearn.Alg_1_1_EA(n, iter)
```
#### (1+1)-EA≠
   ```python
   EvoLearn.Alg_1_1_EA(n, iter, strict=True)
   ```
#### RLS
   ```python
   EvoLearn.Alg_1_1_EA(n, iter, RLS=True)
   ```
#### RLS≠
   ```python
   EvoLearn.Alg_1_1_EA(n, iter, strict=True, RLS=True)
   ```
#### (μ+1)-EA
   ```python
   EvoLearn.Alg_mu_1_EA(n, iter, mu)
   ```
#### (1+λ)-EA
   ```python
   EvoLearn.Alg_1_lambda_EA(n, iter, lambda_)
   ```
#### (μ+λ)-EA
   ```python
   EvoLearn.Alg_mu_lambda_EA(n, iter, lambda_, mu)
   ```
#### SEMO
   ```python
   EvoLearn.Alg_SEMO(n, iter) 
   ```
#### GSEMO
   ```python
   EvoLearn.Alg_SEMO(n, iter, global_=True) 
   ```

## UBoolean函数类

#### OneMax问题
   $$f(s)=\sum^n_{i=1}s_i$$
#### LeadingOnes问题
   $$f(s)=\sum^n_{i=1}\prod^i_{j=1}s_j$$
#### Peak问题
   $$f(s)=\prod^n_{i=1}s_i$$
#### Trap问题
   $$f(s)=c\cdot\prod^n_{i=1}s_i-\sum^n_{i=1}s_i$$
#### LOTZ问题
   $$f(s)=(\sum^n_{i=1}\prod^i_{j=1}s_j,\sum^n_{i=1}\prod^n_{j=i}(1-s_j))$$
#### COCZ问题
   $$f(s)=(\sum^n_{i=1}s_i,\sum^{n/2}_{i=1}s_i+\sum^n_{i/2+1}(1-s_i))$$
