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
print("~fin~")
