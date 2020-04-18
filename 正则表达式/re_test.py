"""
.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式

re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	匹配a或b

贪婪模式
非贪婪模式 .? 量词加？

边界匹配：
^	匹配字符串的开头
$	匹配字符串的末尾。
\b	匹配一个单词边界，也就是指单词和空格间的位置。
例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。

\B	匹配非单词边界。'er\B'
能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。

\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。

"""
import re
txt = '林志玲19岁，迪丽热巴18岁，王欣源8岁'
# 使用compile方法
partern = re.compile('\d+')
reslut = re.findall(partern,txt)
print(reslut)
# 不使用编译方法
reslut2 = re.findall('\d+',txt)
print(reslut2,type(reslut2))
#
txt_3 =' tom Jimmy 1ALice 9090'
reslut3 = re.findall(r'[a-zA-Z]\w+',txt_3)
print(reslut3)

# match重头开始匹配  match对象
partern_txt4 = re.compile('[a-zA-Z]\w+')
txt_4 =' tom Jimmy 1ALice 9090'
reslut4 = partern_txt4.match(txt_4)
print(reslut4)
reslut5 = partern_txt4.search(txt_4)
print(reslut5)

reslut6 = partern_txt4.finditer(txt_4)
print(reslut6)
for i in reslut6:
    print(i)

re.split('\W','GOOD MORNING')
# =====数字换pop
ords = 'ORD001,ORD002,ORD003'
print(re.sub(r'\d+','pop',ords))