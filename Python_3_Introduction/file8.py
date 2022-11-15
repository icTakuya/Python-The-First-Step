# tarfileの圧縮展開
# tarfileはwindowsでいうzip
import os
import pathlib
import tarfile

# # test_dirフォルダを作成して中にtest.txtを作成して、testと書き込む
os.mkdir('test_dir')
pathlib.Path('test_dir/test.txt').touch()
with open('test_dir/test.txt', 'w') as f:
    f.write('test')

# # test_dirフォルダ内にsub_dirフォルダを作成して中にsub_test.txtを作成して、subと書き込む
os.mkdir('test_dir/sub_dir')
pathlib.Path('test_dir/sub_dir/sub_test.txt').touch()
with open('test_dir/sub_dir/sub_test.txt', 'w') as f:
    f.write('sub')

# tarファイル作成
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# tarファイル展開
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tr, path="test_tar")
    # ファイルの中身確認
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())