# @2019.08.26
# 等等 似乎 numpy 也有数组
# numpy 的多维数组对象是怎么实现的来着？ 过后赶紧看吧
# 先看看 python 语法对 numpy 数组的循环吧
# ---
# 没错，语法是 OK 的，只不过 numpy 实现了一套子类型

import numpy as np

narr = np.array([[1,2,4],[3,5,8],[7,8,12]])

for sub in narr:
    print(type(sub))
    for ob in sub:
        print("" + str(type(ob)) + " ~ " + str(ob))
        
for i in range(len(narr)):
    for j in range(len(narr[i])):
        print(narr[i][j])

