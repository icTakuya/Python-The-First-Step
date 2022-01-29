# クラスの定義 
# (object)はPython3ではなくてもよいが、ベースクラスは継承などの関係から書いておいたほうが良い
class Person(object):
    # コンストラクタ。selfは自分自身、必ず入れる
    def __init__(self, name):
        self.name = name
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
    def run(self, num):
        print('run' * num)
    # デストラクタ。終了後に実行される
    def __del__(self):
        print('good bye')

# オブジェクト生成
person = Person('lee')
person.say_something()

# 明示的にデストラクタを実行したいときに使用
# del person

print('########')
