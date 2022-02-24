class Animal:
    # 静态变量,每个对象都会及继承这个值
    # Animal 不会受到印象
    count = 10

    def eat(self):
        print('吃饭')


# 会继承 方法 eat,也可以重写
class Bird(Animal):
    def sing(self):
        print("bird is sing")


class Bird2(Animal):
    def sing(self):
        print("bird2 is sing")

    # 类方法可以访问类
    @classmethod
    def test1(cls):
        print('类方法')

    @staticmethod
    def test2():
        print("静态方法")


bird = Bird()
print(bird.count)
print(Animal.count)
bird.eat()
bird.sing()
bird2 = Bird2()
bird.count = 20

print(bird.count)
print(Animal.count)

print(bird2.count)
