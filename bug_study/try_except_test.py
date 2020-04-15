stu = {
    'name':'迪丽热巴',
    'age':20,
    'score':[98,76,61]
}
# print(stu['name'])
# print(stu['score'][21])
try:
    print(stu['Name'])
    print(stu['score'][21])
# except KeyError:
#     print('学生姓名错误！')
# except IndexError:
#     print('学生成绩超出异常！')
# except (KeyError,IndexError):
#     print('键值或者索引错误')
except Exception:
    print('有异常！')
else:
    print('正确输入！')

