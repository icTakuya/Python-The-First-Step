# ファイルの読み込み
import chunk

s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'w') as f:
#     f.write(s)

with open('test.txt', 'r') as f:
    # print(f.read())
   
    while True:
        # line = f.readline() #列ごとに読み込む
        # print(line, end='')
        
        chunk = 2 # 2文字ごとに読み込む
        line = f.read(chunk)
        print(line)
        
        if not line:
            break

