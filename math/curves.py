
# coding: utf-8

# # 平面曲线: 圆

# In[4]:

import numpy as np;
import matplotlib.pyplot as plt;
get_ipython().magic(u'matplotlib inline')

# 与x轴的夹角
alpha = np.linspace(0, 2*np.pi, 360);
#半径
r = 4;
# 圆心
cx = 2;
cy = -2;


# 调整图片大小与坐标范围, 防止画出来的圆变形
plt.figure(figsize = (4,4));
xlimstart = int(np.floor(cx - 1.2*r));
xlimend = int(np.ceil(cx + 1.2*r));
ylimstart = int(np.floor(cy - 1.2*r));
ylimend = int(np.ceil(cy + 1.2*r));
plt.xlim(xlimstart, xlimend);
plt.ylim(ylimstart, ylimend);

# 画图
def circle(alpha):
    x = r * np.cos(alpha) + cx;
    y = r * np.sin(alpha) + cy;
    return (x, y);

(x, y) = circle(alpha);
plt.plot(x, y, '-');


# 去掉右边框与上边框
ax = plt.gca();
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#设定标度文字相对于坐标轴的位置
ax.xaxis.set_ticks_position('bottom');
ax.yaxis.set_ticks_position('left');

# 设定坐标轴位置: 最熟悉的原点十字.
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))


# 画出圆心
plt.scatter([cx], [cy], 50,color = 'red');

# 标出圆心位置
## 画虚线
plt.plot([cx, cx],[cy, 0], color ='green', linewidth=0.5, linestyle="-.");
plt.plot([cx, 0],[cy, cy], color ='green', linewidth=0.5, linestyle="-.");
## 显示坐标值
xticks = range(xlimstart, xlimend, (xlimend-xlimstart)/5);
yticks = range(ylimstart, ylimend, (ylimend-ylimstart)/5);

## 加上圆心的坐标显示
xticks.append(cx);
yticks.append(cy);
## 删除原点的坐标显示
if(xticks.count(0)):xticks.remove(0);
if(yticks.count(0)):yticks.remove(0);
plt.xticks(xticks);
plt.yticks(yticks);

#画出半径
plt.plot([cx, x[-20]],[cy, y[-20]]);
#标注半径长度
note = 'r={0}'.format(r);
ax.annotate(note, xy=((x[-20]), (y[-20])), xycoords='data',
                horizontalalignment='center', verticalalignment='center');

plt.savefig("./circle.png")


# # 空间曲线: 螺旋线

# In[22]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

t = np.linspace(-2, 5, 100)*np.pi;
r = 1;
x = r * np.cos(t);
y = r * np.sin(t);
z = t;
ax.plot(x,y,z);

plt.savefig('../spiral.png')




