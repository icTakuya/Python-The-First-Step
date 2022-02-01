# ファイルの作成
f = open('test.txt', 'w')
f.write('Test\n')
# printでもかけるがwriteのほうが細かく調整可能
# print('I', 'am',  'print', sep='#', file=f)
f.close() # openしたら必ずcloseする

# withステートメントでファイルをopenする
with open('test.txt', 'w') as f:
    # withインデント内に表記すればcloseは必要ない
    f.write('Test\n')