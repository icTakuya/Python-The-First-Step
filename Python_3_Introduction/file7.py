# ファイル操作 だいたいこの４つのライブラリでできるので覚えておくといい
import os
import pathlib
import glob
import shutil
# 上から一つずつ実行で確認できる

# 1.ファイルまたはディレクトリが存在するかの確認 os
print(os.path.exists('test.txt'))
# 2.ファイルかどうかの確認
print(os.path.isfile('test.txt'))
# 3.ディレクトリかどうかの確認
print(os.path.isdir('design'))

# 4.名前の変更
os.rename('test.txt', 'renamed.txt')

# 5.symlink(リンクしているファイル)
os.symlink('rename.txt', 'symlink.txt')

# 6.ディレクトリの作成
os.mkdir('test_dir')
# 7.ディレクトリの削除
os.rmdir('test_dir')

# 8.ファイルの作成 pathlib
pathlib.Path('empty.txt').touch()
# 9.ファイルの削除
os.remove('empty.txt')

# 10.ディレクトリ作成して、その中にディレクトリ作成をして、中身を確認する
os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))

# 11.test_dir2の中にファイル作成して、＊で中身確認する glob
pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))

# 12.コピーして作成 shutil 中身を確認するとリストで返してくれる
shutil.copy('test_dir/test_dir2/empty.txt', 
        'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))

# 13.フォルダーを中身を含めて削除。注意！ shutil
shutil.rmtree('test_dir')

# 現在のディレクトリ確認 os
print(os.getcwd())