
import tensorflow as tsf
import os

# poor machine, T-T
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

#
# 第一个 tensorflow demo, 来自书上的
#

print("@@ here we go @@!!")
# 定义常量向量 a， b
a = tsf.constant([1.0, 2.0], name="a")
b = tsf.constant([2.0, 3.0], name="b")

# 向量相加
c = a + b

# 需要执行
sess = tsf.compat.v1.Session()
res = sess.run(c)

## 打印结果
print(a)
print(b)
print(c)
print(res)
