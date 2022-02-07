# これらはあくまで１例であり、会社やチームによってルールが違う場合はあるので注意


# セミコロンがなくてもわかりやすいコードをかく
x = 1;
y = 2;


# 80字超えたら改行する
def test_func(x, y, z, 
              fghjggkjhgklhkhhlkjlkjlkhklhklhkljkljlkjkljlkjlkj='test'):
    """
    # コメントのURLは例外的にOK
    See details at: http://kjfh;gklhdkshkldhgklhlkhgjkhjkhkjhjkhklhlkhlkhlkhlhlkhlkhlh
    """
    print('test')


# 意味のない（）は使用しない
# スペースの入れ方。関数のデフォルト引数などは入れない
if (x):
    x = {'test': 'ttt'}

    x = 200
    yyyyyyyyyy = 500
    zzzzzzzzzzzzzzz = 700


# 改行
from hashlib import new
import os
from unittest.mock import DEFAULT
# 1
# 2
class T(object):
# 1
# 2
    def __init__(self):
        pass
# 1
    def s(self):
        pass
# 1
# 2
class U(T):
    pass 


# 文字列の結合
word = 'hello'
word2 = '!'

new_word = '{} $$$$$$ {}'.format(word, word2)
new_word = word + word2

long_word = ""
for word in ['hjkshkh', 'lajfkljlkfhjl', 'ghgggjkk']:
    long_word.append("{}hgjgkjllh".format(word))
new_long_word = ''.join(long_word)


# シングルクォート、ダブルクォートの違いは企業やプロジェクトのルールによる
print('kjkhlkjhl')
print("kjkhl'kjhl") #中に'

"jkhjkh {} kgkgkhl".format('test') # 中に｛｝


# TODO (名前 or email)


# if文は1行で記述しない
if x:
    print('exit')
else:
    print('else')

if x: print('exit')
else: print('else')


# クラス名は_で記述しないで大文字にする。キャメルケース
# プロパティ
class HappilyEverAfter(object):
# 関数名は_でつなぐ。スネークネーム
    def dont_give_up(self):
        pass


# グローバル変数の宣言はすべて大文字で＿でつなぐ
DEFAULT_MOVIE_NAME = 'Up'


y = None
x = 1 if y else 2
print(x) # 2

y ='hhjh'
x = 1 if y else 2
print(x) # 1