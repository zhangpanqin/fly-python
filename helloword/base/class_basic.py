class People:
    # 类比构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性,只能在类中修改
        self.__var = 10
        self.__birthday = 20

    # 对象方法
    def sayhi(self):
        print("Hi,my name is {}, age is {}".format(
            self.name, self.age
        ))

    def getvar(self):
        return self.__var

    # 控制修改属性调用方法
    @property
    def birthday(self):
        return self.__birthday

    # 修改私有变量,通过 someone.birthday= 20 ,通过这种方式就可以对参数进行校验
    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday


someone = People('zhangSan', 21)
someone.sayhi()
someone.age = 22
#
People.__var = 20
print(someone.getvar())
# 20
print(someone.birthday)
someone.birthday = 30
# 30
print(someone.birthday)
