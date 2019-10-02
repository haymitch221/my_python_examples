import phy_first as f

print(f.getGreeting("James"))
print(f.getGreeting())
print(f.getBye("Tom")("next day"))
print(f.say(f.getBye("Petter")))
print(f.say())

print(f.twoParam)
print(f.twoParam())
print(f.twoParam(a = "aaa", b = "bbb"))
print(f.twoParam(a = "aaaa"))
print(f.twoParam(b = "bbbb"))
print(f.twoParam("aaaaaa"))

print("---·---·---·---")
print(f.multiParam("3", 3, 4, c = "aa", a = "dwfq"))
print("---·---·---·---")
# 等于 f.logger(f.workout)("swim")
f.workout("swim")
print("---·---·---·---")
# 等于 f.loggerGood("asdf")(f.workoutGood)("jump")
f.workoutGood("jump")


print("~fin~")
