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