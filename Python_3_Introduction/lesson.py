# 会社によってフルパスもしくはモジュールからimportする

# 1.フルパス
import lesson_package.tools.utils
r = lesson_package.tools.utils.say_twice('hello')
print(r)

# 2.lesson_package.toolsのutilsをimportする
from lesson_package.tools import utils
r2 = utils.say_twice('hello')
print(r2)

# 3.lesson_package.tools.utilsのsay_twiceメソッドをimportする
# これはどこのsay_twiceかわからずコンフリクト発生の原因になるので、好まれない
from lesson_package.tools.utils import say_twice
r3 = say_twice('hello')
print(r3)

# 4.as 〜とすることで〜として扱えるが、どの様なモジュールかわからなくなってしまうため、こちらもすすめられていない。しかしモジュール名が極端に長い場合は使用されることもある
from lesson_package.tools import utils as u
r4 = u.say_twice('hello')
print(r4)