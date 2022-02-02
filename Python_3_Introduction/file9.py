# zipfileの圧縮展開
import os
import pathlib
import glob
import zipfile


with zipfile.ZipFile('test.zip', 'w') as z:
# 1.下記のように指定して作成することの可能だが3のほうがまとめてできる
    # z.write('test_dir')
    # z.write('test_dir/test.txt')

# 2.フォルダとファイル追加
    os.mkdir('test_dir/sub_dir/subsub_dir')
    pathlib.Path('test_dir/sub_dir/subsub_dir/subsub_test.txt').touch()
    
# 3.zip作成
    # ** recursive=Trueとすると階層内フォルダとファイルを確認してくれる
    for f in glob.glob('test_dir/**', recursive=True):
        print(f) # 確認用
        z.write(f)

# 4.読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')
# 5.指定のファイルのみ確認
    with z.open('test_dir/test.txt') as f:
        print(f.read())