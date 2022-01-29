from lesson_package.talk import human
from lesson_package.talk import animal

# 次のように* を使用することもできるがimportするフォルダの__init__ファイルに__all__を追加しなければならないため、すすめられていない
# from lesson_pakage.talk import *

print(animal.sing())
print(animal.cry())

print(human.sing())
print(human.cry())


# バージョンアップなどで変更した際にtry exceptを使用すればエラーなく実装できる
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils
print(utils.say_twice('word'))