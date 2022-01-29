# 組み込み関数（ビルドイン関数）
# https://docs.python.org/ja/3/library/functions.html

# printやglobalsは組み込み関数としてあらかじめ入っているが本来は次のようになっている
import builtins
builtins.print('Hello World!')


# 並び替え
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# for文で並べると順番通り
for key in ranking:
    print(key)

# 点数順に並び替えたい場合はsorted関数を使用してgetをキーにする
# print(ranking.get('B'))

print(sorted(ranking, key=ranking.get, reverse=True))