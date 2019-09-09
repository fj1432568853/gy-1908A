a = 1
print(type(a))
b = 1.1
print(type(b))
c = 's'
print(type(c))
l = [2,3,4,5,6]
print(l)
print(type(l))
t = (1,2,)
print(t)
print(type(t))
d = {'姓名':'牛组长','籍贯':'火星人'}
print(d)
print(type(d))
a = 5
b = 4
print(a+b*b)
print(1/3)
print(4 in l)
print('姓名' in d)

g = 5
if (g == 5 ):
    print('哪有那么多如果呀')
else:
    print('睡吧')


g = 70
if(g >= 80):
    print("回家被打一顿")
elif(g >= 60):
    print("回家被打2顿")
else:
    print('一切都不好了')


for i in range(100):
    if(i%2 == 1):
        print(i)



for i in range(100):
    if(i==5):
        break
    print(i)


for i in range(100):
    if(i%5==0):
        continue
    print(i)

# 求出1+2+3.。。+100和
s = 0
for i in range(1,101):       
    s += i
print(s)

# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)










