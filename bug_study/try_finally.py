# f = open('1.txt', 'r', encoding='utf8')
try:
    f = open('11.txt', 'r', encoding='utf8')
    txt = f.read()
    print(txt)
    # a,b=10,0
    # print(a/b)
except Exception:
    print('文件打开错误！')
finally:
    print('文件关闭')
    f.close()
