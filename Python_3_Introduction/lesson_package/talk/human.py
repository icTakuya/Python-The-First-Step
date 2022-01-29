from lesson_package.tools import utils
# 次のような書き方もできるが、進められていない
# from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')