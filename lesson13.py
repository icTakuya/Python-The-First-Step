class Person(object):
   
    # クラス変数はすべてのオブジェクトで共有される
    kind = 'human'

    def __init__(self, name):
        # self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind) # 呼び出しにはself.が必要

a = Person('A')
a.who_are_you()
a = Person('B')
a.who_are_you()

# リストの場合（良くないパターン）
class T(object):

    words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')
# c.wordsの出力でもクラス変数は共有されているため、dの追加分も表示される
print(c.words)


# 上記の場合予期せぬ追加変更になってしまう
class S(object):

    def __init__(self): #リストなどはこの様にコンストラクタ内に記載する
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = S()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = S()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)
