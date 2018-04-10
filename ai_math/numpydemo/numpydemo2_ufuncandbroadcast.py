import numpy as np

"""
ufunc演示
运算都是在element-wise
"""
# x = np.linspace(0, 6.28, 1000).reshape(-1, 5)
# y = np.sin(x)
# z = x + 100
# logx = np.log2(x)

"""
broadcast演示
待扩展维度，形状必须是1才可以扩展
"""

# x1 = np.arange(3).reshape((-1, 1))
# x2 = np.arange(3)
#
# print(x1 + x2)

# x1 = np.arange(4).reshape((2, 2))
# x2 = np.arange(6).reshape((-1, 2))
# print(x1 + x2)

x1 = np.arange(12).reshape((3, 4))
x2 = np.arange(3).reshape((1, -1))
print(x1 + x2)