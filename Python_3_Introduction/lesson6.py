# __name__の関係
# 他で読み込まれた場合は__main__にならない

# import config

# print('lesson:', __name__)


import lesson_package.talk.animal

# 開発では下記の様に記述して、他から利用されたときに実行されないようにする
def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main_':
    main()