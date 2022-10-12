<!--
 * @Author: Derry
 * @Date: 2022-09-29 17:07:11
 * @LastEditors: Derry
 * @Email: drlv@mail.ustc.edu.cn
 * @LastEditTime: 2022-10-12 23:55:03
 * @Description: None
-->

# Evolutionary Learning 演化学习

## 演化学习算法

### 演化算法类

```python
EvoLearn(f=lambda x: np.sum(x))
```

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

### UBoolean函数类

```python
UBoolean()
```

#### OneMax问题

最大化一个解中1-位的个数

$$
f(s)=\sum^n_{i=1}s_i
$$

最优值：$1^n$

```python
UBoolean.OneMax(s)
```

#### LeadingOnes问题

最大化一个解中从首端开始连续1-位的数目

```python
UBoolean.LeadingOnes(s)
```

最优值：$1^n$

$$
f(s)=\sum^n_{i=1}\prod^i_{j=1}s_j
$$

#### Peak问题

在除最优解$1^n$以外的所有解上具有相同的相似度

```python
UBoolean.Peaks(s)
```

最优值：$0$

$$
f(s)=\prod^n_{i=1}s_i
$$

#### Trap问题

在最优解$1^n$之外，最大化一个解中0-位的数目

$$
f(s)=c\cdot\prod^n_{i=1}s_i-\sum^n_{i=1}s_i
$$

最优值：$c - n > 0$

```python
UBoolean.Peaks(s)
```

#### LOTZ问题

目标一：最大化从解的首端开始的连续的1-位的数目（LeadingOnes）

目标二：最大化从解的尾端开始的连续的0-位的数目

帕累托最优解：$0^n, 10^{n-1}, ..., 1^n$

$$
f(s)=(\sum^n_{i=1}\prod^i_{j=1}s_j,\sum^n_{i=1}\prod^n_{j=i}(1-s_j))
$$

```python
UBoolean.LOLZ(s, alpha=0.5)
```

#### COCZ问题

目标一：最大化解中1-位的数目（OneMax）

目标二：最大化解前半部分中1-位的数目和后半部分中0-位的数目之和

帕累托最优解集合：$\{1^{n/2} * ^{n/2}|*∈\{0,1\}\}$

$$
f(s)=(\sum^n_{i=1}s_i,\sum^{n/2}_{i=1}s_i+\sum^n_{i/2+1}(1-s_i))
$$

```python
UBoolean.COCZ(s, alpha=0.5)
```
