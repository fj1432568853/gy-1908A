a = [1,2,3,4,5,6,7,8]


a.append(23)
print(a)

a.insert(2,34)
print(a)

b = [5,6,7,8,9]
a.extend(b)
print(a)
print(b)

print(a.pop(3))
print(a)

print(a.pop())
print(a)

a.remove(34)
print(a)






