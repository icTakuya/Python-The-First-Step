from lesson_package.tools import utils

def sing():
    return 'kjahikfgseruihgolh'

def cry():
    return utils.say_twice('ijdbiuahgihaojapo')

# 他で呼び出された場合に以下があると実行されない
if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)