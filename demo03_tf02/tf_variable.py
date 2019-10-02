import tensorflow as tf
import os

# poor machine, T-T
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

#
# 定义 tensorflow 的 变量
#
print("@@ here we go @@!!")

# 定义变量，同时指定变量的初始化方式（这里并没有真正被初始化）
v1 = tf.Variable(tf.random_normal([2, 3], stddev=2))
v2 = tf.Variable(tf.random_normal([2, 3], stddev=2))
v3 = v1 + v2

with tf.compat.v1.Session() as ss:
    print(type(v1.initializer))
    print(type(tf.compat.v1.global_variables_initializer()))
    # 需要一个个手动执行变量的初始化方法
    # ss.run(v1.initializer)
    # ss.run(v2.initializer)
    # 或者使用这个，初始化所有变量（当变量很多时，会方便许多）
    ss.run(tf.compat.v1.global_variables_initializer())
    res = ss.run(v3)

print(res)
