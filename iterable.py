# Iterable 資料型態
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代的資料:
# for x in 'abc':
#     print (x)

# for x in [3, 5, 2]:
#     print (x)

# for x in {"a", "test", 3, 10}:
#     print (x)

# dict = {"a":3, "x":5}
# for key in dict:
#     print (key)
#     print (dict[key])

#內建函式
# max(可疊代資料)
# result=max([10, 2, 30, 1])
# print(result)
# result=max('xaz')
# print(result)
# result=max({10, 200, 30, 1})
# print(result)
# result=max({"x":3, "a":4})
# print(result)

# sorted(可疊代資料)
result=sorted("cba")
print(result)
result=sorted({10, 2, 100, -5})
print(result)
result=sorted([10, 2, 30, 1])
print(result)
result=sorted({"x":3, "a":4})
print(result)