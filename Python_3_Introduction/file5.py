# テンプレート
import string

from sympy import content

s = """\
Hi $name.

$contents

Have a good day
"""

# sを読み込み専用としてtに代入しておけばsは変更されなくてすむ
t = string.Template(s)
contents = t.substitute(name='Yujin', contents='How are you?')
print(contents)


# 上記を他のファイルから読み込む形にする(Sの内容を別フォルダdesignのemail_template.txtに入れておく)
# その様に対応することで開発中の間違いを減らせる
with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Yujin', contents='How are you?')
print(contents)
