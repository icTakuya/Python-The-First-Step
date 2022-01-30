class Person(object):
   
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind
    
    # 下記のようにclassメソッドとして表記するとオブジェクト生成しなくとも使用可能
    # @classmethod
    # def what_is_your_kind(cls):
    #     return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))


a = Person()
print(a) #オブジェクトですよと返ってくる
print(a.x) # 100
print(a.kind)
print(a.what_is_your_kind())


print('#########')
b = Person #オブジェクト生成しない
print(b)
# print(b.x) オブジェクトではないのでアクセスできない
print(b.kind) #クラス変数はアクセスできる
# print(b.what_is_your_kind()) オブジェクト化してないのでselfが自分自身でない

# クラスメソッドの使用
# print('#########')
# print(Person.kind)
# print(Person.what_is_your_kind())

# スタティックメソッドの使用
Person.about(1999)