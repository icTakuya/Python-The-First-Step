# 標準ライブラリは自分で読み込む必要がある
# https://docs.python.org/ja/3/library/

# 文字列の個数を数えたい
s = "kdgsiuhklghdlkghuish"

# forを使用して表示する場合
d ={}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

# setdefault関数を使用
d ={}
for c in s:
    # cがなければ0になる
    d.setdefault(c, 0)
    d[c] += 1
print(d)

# collectionsのdefaultdictを使用した場合
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['g'])