b = 'hdgadgadjhdgajdhabdja'
print(b[::3])
print(b[1::3])


d = 'weqweqwe,qweqw,qwad,dasda'
print(d.split(','))

f = 'weqwdqqda     wdccada   wdads'
print(f.replace(" ",''))


# GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
s = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
l = s.split(' ')
qingqiufangfa = l[0]
print('请求方法：'+ qingqiufangfa)