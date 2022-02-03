# tempfile
import tempfile

# #Temporary=一時的なもの 
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# テンプファイル作成
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name) #パス ターミナルのcatコマンドで入力すると中身がわかる
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# テンポラリーフォルダ
with tempfile.TemporaryDirectory() as td:
    print(td) #パス

# テンプフォルダ作成
tmp_dir = tempfile.mkdtemp()
print(tmp_dir) #パス