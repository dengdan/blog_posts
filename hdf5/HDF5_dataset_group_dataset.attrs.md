
HDF5, 大量(海量?)数据存储的一种解决方案. HDF的全称是Hiearchical Data Format, 5是版本号(未考证过TODO). 一个HDF5文件操作起来就像一个独立的文件系统.  (TODO, I/O特性, 是事件驱动的吗?)


```python
import h5py
import numpy as np
```

# 创建一个HDF5文件


```python
f = h5py.File("/home/dengdan/temp/no-use/hdftest.hdf5", "w")
```

它可以存储两类数据对象:
1. dataset, 类比于文件系统的文件, 可以用操作list/ndarray的方式来操作它
2. group, 类比于文件系统的文件夹. , 可以用操作dict的方式来操作它

## dataset


```python
dset = f.create_dataset(name = "/mydataset1", shape = (100,100), dtype= np.uint8)
print dset.shape
```

    (100, 100)



```python
print dset.dtype
print dset[:]
```

    uint8
    [[0 0 0 ..., 0 0 0]
     [0 0 0 ..., 0 0 0]
     [0 0 0 ..., 0 0 0]
     ..., 
     [0 0 0 ..., 0 0 0]
     [0 0 0 ..., 0 0 0]
     [0 0 0 ..., 0 0 0]]


hdf5以POISX文件系统的风格存储数据对象, 每个对象都有自己的名字, 格式与linux文件路径相同


```python
print dset.name
```

    /mydataset1


## group


```python
grp = f.create_group("subgroup")
```


```python
print grp.name
```

    /subgroup



```python
dset2 = grp.create_dataset("another_ds", (50,), dtype='f')
print dset2.name
```

    /subgroup/another_ds


创建dataset时若指定了上级group, 会自动创建


```python
dset3 = f.create_dataset('subgroup2/dataset_three', (10,), dtype='i')
print dset3.name
```

    /subgroup2/dataset_three


整个hdf文件就像一个大字典,读取dataset时可以根据它的name从中直接取出.


```python
dset3_read = f['subgroup2/dataset_three']
dset3 == dset3_read
```




    True




```python
for name in f:
    print name
    # 只会显示根目录下的对象.
```

    mydataset1
    subgroup
    subgroup2



```python
def visit_file(name):
    print name
f.visit(visit_file) 
    # 显示所有对象.
```

    mydataset1
    subgroup
    subgroup/another_ds
    subgroup2
    subgroup2/dataset_three


# attrs
dataset对象可以有自己的属性, 但所有属性数据的长度加起来不能超过64K, 包括属性名字.


```python
dset.attrs['length'] = 100
dset.attrs['name'] = 'This is a dataset'
```


```python
for attr in dset.attrs:
    print attr, ":", dset.attrs[attr]
```

    length : 100
    name : This is a dataset


<hr>
# Reference
* http://docs.h5py.org/en/latest/quick.html


```python

```
