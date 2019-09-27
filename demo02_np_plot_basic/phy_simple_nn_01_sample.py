import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# simple nn
# 只是展示效果
# TODO：
# 训练的过程应该有一个线程开启，写出训练后的参数（weights）
# 应用的方法获取训练后的参数
def proc(x, y):
    # seed random numbers to make calculation
    # deterministic (just a good practice)
    np.random.seed(1)

    # initialize weights randomly with mean 0
    weights=2*np.random.random((3,1))-1
    # weights=np.array([[ 9.67299303], [-0.2078435 ], [-4.62963669]])

    for iter in range(10000):
        # forward propagation
        l0=x
        l1=nonlin(np.dot(l0,weights))
    
        # how much did we miss?
        l1_error=y-l1

        # multiply how much we missed by the 
        # slope of the sigmoid at the values in l1
        l1_delta=l1_error*nonlin(l1,True)

        # update weights
        weights+=np.dot(l0.T,l1_delta)

    print("weights: ", weights)
    return l1

print("Output After Training:")

# input dataset
x=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
# expecting output dataset            
y=np.array([[0,0,1,1]]).T

res = proc(x, y)
print("result: ", res)
