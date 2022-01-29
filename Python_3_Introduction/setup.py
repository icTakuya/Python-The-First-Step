# packageフォルダと実行ファイルのある階層にsetup.pyを作成して、ターミナルでpython setup.py sdistを実行するとMANIFESTとdistフォルダが作成されフォルダ内にtar.gzファイルが作成される

from distutils.core import setup

setup(
    name='python_programming',
    version='1.0.0',
    packages=['lesson_package', 'lesson_package.talk', 'lesson_package.tools'],
    url='',
    license='Free',
    author='icTakuya',
    description='Sample package'
)