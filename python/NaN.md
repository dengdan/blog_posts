
NaN, Not a Number, 非数. 它即不是无穷大, 也不是无穷小, 而是python/numpy/... 觉得无法计算时返回一个符号(自己的推测, 未考证(TODO)). 


```python
import numpy as np
```

# 无穷大减无穷大会导致NaN


```python
a = np.infty
```


```python
print a - a
```

    nan



```python
print a * a, a * a - a
```

    inf nan


# 无穷大乘以0或无穷小或除以无穷大会导致NaN


```python
print a * 0
```

    nan



```python
print a * 1/ a
```

    nan



```python
print a / a
```

    nan



```python
print a / 1
```

    inf



```python
print a / 1
```

    inf


** 总结起来就是, 涉及到无穷大的四则运算, 若无法确定运算结果仍为无穷大, 那么运算结果就是一个NaN.**

另外很明显的是:
# 有NaN参与的运算, 其结果也一定是NaN


```python
b = np.nan
```


```python
print b + 1
```

    nan



```python
print b - b
```

    nan


# NaN != NaN


```python
print b == b
```

    False


<hr>
markdown由jupyter notebook生成. [notebook](https://github.com/dengdan/blog_posts/blob/master/python/NaN.ipynb)


```python

```
