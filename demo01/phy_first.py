import time

print("preparing phy_first helloooo!!!")

# 简单的函数定义
def getGreeting(who = "nobody"):
    return "hellloo " + who

# 返回 lambda 的函数定义
def getBye(who = "anyone"):
    return lambda time: "bye " + who + ", till " + time 

# lambda 函数作为参数的函数定义
def say(what = lambda when: "" + when + " is a good"):
    return what("tomrrow")

# 带默认参数的函数定义
def twoParam(a = "aa", b = "bb"):
    return "" + a + " !!! " + b

# 自定义数目的参数
# 调用时， 按照顺序 *a 的部分枚举值， **b的部分枚举键值对即可，不要交叉
def multiParam(*a, **b):
    print(a)
    print(b)

# 装饰器函数
def logger(func):
    def wrapper(*args, **kwargs):
        print("logger start")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("logger end: The func '{}' used {}s.".format(func.__name__, end-start))
        print("logger return:", result)
        return result
    return wrapper

# 带参数的装饰器函数
def loggerGood(arguments):
    def loggerInner(func):
        def wrapper(*args, **kwargs):
            print("very good logger start")
            print("very good logger is logging", arguments)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("very good logger end: The func '{}' used {}s.".format(func.__name__, end-start))
            print("very good logger return:", result)
            return result
        return wrapper
    return loggerInner

# 一个被简单装饰的函数
@logger
def workout(a = "running"):
    print(a, "...", "begin")
    print(a)
    print(a, "...", "done")
    return "okkk"

# 一个被带参数装饰器装饰的函数
@loggerGood("asdfg")
def workoutGood(a = "running"):
    print(a, "...", "begin！")
    print(a)
    print(a, "...", "done！")
    return "okkk！"