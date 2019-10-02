import tensorflow as tf
import os

from numpy.random import RandomState

# poor machine, T-T
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

# 实现第一个简单的神经网络
# 第一步：神经网络的结构
#  输入层特征数features，输出层
#  隐藏层结构（层数hidden layers）
#  简单的神经元先直接使用特征权重成绩的和
#  初始权重随机即可
# 第二步：tf 的实现神经网络的过程
#  定义输入变量节点（建议用placeholder）
#  定义各隐藏层，由权重矩阵（多维数组表示，输出层特殊为一维数组）
#  定义表示一次向前传播的计算（比如变量依次与权重矩阵相乘）
# 第三步：损失函数、反向传播算法的定义
# 第四步：获取输出，用会话初始化所有变量
# 第五步：定义循环次数steps，用循环表示多次训练
#  在循环中用会话跑反向传播算法

# 简单的三层神经网络：输入层，一层隐藏层，输出层
# 目标是给二维数据分类（两类）

# 定义输入层
x = tf.compat.v1.placeholder(tf.float32, shape=(None, 2), name = 'x-input')
# 定义输入结果（即用于与预测结果比较的真实结果）
y_ = tf.compat.v1.placeholder(tf.float32, shape=(None, 1), name = 'y-input')

# 一层隐藏层和输出层
w1 = tf.Variable(tf.random.normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random.normal([3, 1], stddev=1, seed=1))

# 第一层隐藏层计算的中间结果向量
r1 = tf.matmul(x, w1)
# 输出层计算到结果值
y = tf.matmul(r1, w2)

# 定义损失函数和反向传播算法
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(
    y_ * tf.math.log(tf.clip_by_value(y, 1e-10, 1.0))
    + (1 - y_) * tf.math.log(tf.clip_by_value(1-y, 1e-10, 1.0))
    )
train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 生成随机数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]
# 定义训练次数，每次训练的数据量
steps = 5000
batch_size = 8

# 创建会话开始训练
with tf.compat.v1.Session() as ss:
    # 初始化所有参数
    ss.run(tf.compat.v1.global_variables_initializer())
    # 打印训练前的初始权重
    print(ss.run(w1))
    print(ss.run(w2))
    # 开始训练
    for i in range(steps):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        ss.run(train_step, feed_dict={x:X[start:end], y_:Y[start:end]})
        if i % 1000 == 0:
            total_cross_entropy = ss.run(cross_entropy, feed_dict={x:X, y_:Y})
            print("After %d train step(s), cross_entropy on all data is %g" % (i, total_cross_entropy))
    # 打印训练之后被优化的权重
    print(ss.run(w1))
    print(ss.run(w2))



