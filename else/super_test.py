# -*-coding:utf8-*-


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()   # Python3 可使用 super().greet()
        print('WangWang...')


if __name__ == '__main__':
    a = Animal('animal')
    # a.greet()
    d = Dog('wang cai')
    d.greet()


