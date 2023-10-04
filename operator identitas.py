data1 = [1, 2, 3]
data2 = list([1, 2, 3])
data3 = data1

print("id data1=", id(data1))
print("id data2=", id(data2))
print("id data3=", id(data3))

print(data1)
print(data2)

print("data1 == data2=", data1 == data2)
print("data1 == data3=", data1 == data3)

print("data1 is data2=", data1 is data2)
print("data1 is data3=", data1 is data3)

print("data1 is not data2=", data1 is not data2)
print("data1 is not data3=", data1 is not data3)
