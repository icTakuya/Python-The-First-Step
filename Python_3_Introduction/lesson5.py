# importする際の記述の注意点

# まとめて記述しない
# import collections, sys, os

# 1.標準ライブラリ
# 2.サードパーティ
# 3.自作パッケージ
# 4.ローカルファイル
# 1~4はスペースを開けて記述する。アルファベット順に記述する

import collections
import os
import sys

import termcolor

import lesson_package

import config


# どこにあるか確認する方法
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

# 読み込む順番
print(sys.path)