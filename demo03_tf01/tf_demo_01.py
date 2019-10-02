import tensorflow as tf
import os

# poor machine, T-T
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

#
# 第一个 tensorflow demo, 来自书上的
#

# 两个向量（多维数组）相加
def simpleAdd(arr1, arr2):
    # 定义向量 a， b，并相加
    a = tf.constant(arr1, name="a")
    b = tf.constant(arr2, name="b")
    c = a + b
    # 执行并输出结果
    with tf.compat.v1.Session() as sess:
        res = sess.run(c)
    ## 打印结果
    print(a)
    print(b)
    print(c)
    return res

print("@@ here we go @@!!")
print(simpleAdd(4, 3))
print(simpleAdd(2.1, 3.7))
print(simpleAdd([5.2], [7.4]))
print(simpleAdd([2.1, 5.2, 4.6, 1.9], [3.7, 7.4, 6.5, 3.3]))
print(simpleAdd([[1, 2, 3], [4, 5, 6]], [[2, 5, 5], [6, 9, 13]]))
