def div(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print('除数不能为0')
        return
    return c
print(div(2,0))







