person_x = 99
person_y = 199
person_z = 299
import datetime
class PERSON:
    # def check_salary(self):
    #     pass
    person = []
    def __init__(self, name, birthdate, gender='男',salary=2000):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.salary = salary
        PERSON.person.append(self)

    # 静态方法
    @staticmethod
    def conn_dbs():
        print('连接数据库')

    # cls 等于PERSON
    @classmethod
    def print_all(cls):
        # print(PERSON.person)
        print(cls.person)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value<=0:
            self._salary=0
        else:
            self._salary=value
    # def get_age(self):
    #     return datetime.date.today().year - self.birthdate.year

    # @property
    @property
    def age(self):
        return datetime.date.today().year - self.birthdate.year

    # 装饰器
    @age.setter
    def age(self, value):
        raise ValueError('年龄不能赋值！')

    # def say(self):
    #     print('{}你好!!!'.format(self.name))
    #     return self.name

    # def my_age(self):
    #     print('我今年{}岁了'.format(self.age))
    #     return self.name

    def __str__(self):
        return (f'PERSON {self.name} {self.birthdate} {self.gender} {self.salary}')

    def __repr__(self):
        return (f'PERSON {self.name} {self.birthdate} {self.gender} {self.salary}')


p2 = PERSON('tom', datetime.date(1980, 9, 1))
p1 = PERSON('JIMMY', datetime.date(1989, 9, 1))
# p2.birthdate = datetime.date(1994, 9, 1)
p2.salary = 9000
# p2.age = 30
print(p2)
p2.print_all()
PERSON.print_all()
PERSON.conn_dbs()