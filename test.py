a= [1,2,3,7,8,9]
b =[4,5,6]

a = a+b

print(a)

del a[0]
print(a)
a.append(9)
a.append(9)
a.append(8)
a.append(9)
print(a)

s = set(a)
print(s)

a = list(s)
print(a)