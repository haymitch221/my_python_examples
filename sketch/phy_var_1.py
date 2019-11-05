# 19.11.05
# 实验None、False、True, 都是是大写开头
a = None
b = False
c = True
d = bool("True")
if a is None and not b:
    print("good", a, b)
    print("ok", c, d, type(d))

# 使用 input 得到终端的输入
# 终端的输入类型是str
e = str(input("talk to me: "))
if e == "3":
    print("it is 3")
elif e == "4":
    print("it is 4")
elif e == "5":
    print("it is 5")
else:
    print("thanks")

while(True):
    f = input("> ")
    if str(f) != "":
        print ("right ", f, type(f))
    if f == "bye":
        print ("good bye")
        break



