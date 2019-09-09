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


# 求出100以内的质数

for i in range(2,100):
    f = False # 标记i是否被整除
    for j in range(2,i):
        if(i%j==0):
            f = True #如果i被整除，把f值改成True
            break
    if (not f):
        print(i)


# 打印出九九乘法表（循环嵌套）
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,'=',i*j,'\t',end='')
    print()



# 冒泡排序
a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)


def jia_fa(a,b):
    print(a+b)

jia_fa(4,5)



def aaa(*args,**kwargs):
    print(args)
    print(kwargs)

aaa(1,2,3,4,5,6,a=7,b=8,c=9)


class ClassDemo():
    def aaa(self):
        print('dadadada')

if __name__ == '__main__':
    c=ClassDemo()
    c.aaa()
