# @2019.08.26
# ---
# 循环各种各样的东西
# 集合，列表，元组，字典
# 注意 集合（set）中成员、 dict 的 key 值的类型，是要能 hash 的, 
# 所以不能 hash 的类型有 list，set, dict; 当然可能还有别的
# tuple 是能 hash 的， 但 tuple 包含前面不能 hash 的类型后 tuple 就不能 hash 了；

list1 = [1, 3, 'haha', {"e":3, 5: 'regeg', (12, 'efef'): type(23)}]
set1 = {11, 22, '33', (44, "55", (66, 77, '88'), (99, 'aa'))}
tuple1 = (11, '22', {33 : "33"}, {"44", 55, 66}, [77], [88, 99, "aa"], ("bb"), ("cc",), ("dd", "ee", ), (),)
dict1 = {11: "11", 22: ["22"], '33': {44, "55", '66'}, (77): {"77":77, 88:"88"}, () : 88, (99, "aa",): ("bb", "cc")}

print("\n--------\n")
print("循环 list 用 for in")
for ob in list1:
    print(str(type(ob)) + "～" + str(ob))
    
print("循环 list 用 for range(len)")
for i in range(len(list1)):
    print(str(type(i)) + "～" + str(i) + "～" + str(list1[i]) + "～" + str(type(list1[i])))


print("\n--------\n")
print("循环 set 用 for in")
for ob in set1:
    print(str(type(ob)) + "～" + str(ob))



print("\n--------\n")
print("循环 tuple 用 for in")
for ob in tuple1:
    print(str(type(ob)) + "～" + str(ob))



print("\n--------\n")
print("循环 dict 用 for in")
for key in dict1:
    print(str(type(key)) + "～" + str(key) + ": " + str(dict1[key]) + "～" + str(type(dict1[key])))

