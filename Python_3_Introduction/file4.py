# 書き込み読み込みモード
s = """\
AAA
BBB
CCC
DDD
"""

# w+にする
with open('test.txt', 'w+') as f:
    # print(f.read()) 最初に読み込み飲みをするとw書き込みモードで最初に新しいファイルが用意されるため中身はからになるので注意
    
    f.write(s)
    # 書き込みで最後まで行っているのでseek(0)で一番最初に戻ってからread()
    f.seek(0)
    print(f.read())

# 読み込みモードの場合は先に読み込むファイルがないとエラーになる
with open('test2.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    print(f.read())