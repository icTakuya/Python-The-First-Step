# subprocessでコマンドを実行する。ターミナルのコマンドをPython上で行う
# datetime
import datetime
import subprocess

# os.system('ls')昔はこちらが使われていたが、現在は使用しないこと
subprocess.run(['ls', '-al'])

# 今の日時
now =datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

# 今の年月日
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 時間表示
t = datetime.time(hour=12, minute=24, second=10, microsecond=24)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

# 日時計算
print(now)
d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(seconds=1)
d = datetime.timedelta(microseconds=1)
print(now - d)

# タイムスリープ
import time
print('###')
time.sleep(2) #2秒後
print('####')

# バックアップ作成
import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

with open(file_name, 'w') as f:
    f.write('test')