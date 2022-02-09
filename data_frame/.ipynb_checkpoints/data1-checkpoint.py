# Pandasの基本
# Series=1次元 DataFrame=２次元 のクラス・オブジェクト
# カラム＝行（ヨコ）, インデックス＝行を示す値 列（タテ）

import os

import pandas as pd


# 基本的に打ち込むことはない
# DataFrameの作成
df = pd.DataFrame({'name':['Yujin', 'Xiaoting', 'hikaru'],
              'age':[25, 22, 17],
              'address':['Korea', 'China', 'Japan'],
              'blood type':['A', 'AB', 'O']
            },index=['id-1', 'id-2', 'id-3'])        

# エクセル出力
df.to_excel('data_frame/user_data.xlsx', sheet_name='sample_data')

# Seriesの作成
sr = pd.Series(['Dayeon', 'Mashiro', 'chaehyun'])


# 読み込み
# インデックス列の指定, 読み込みシートの指定
# df = pd.read_excel('user_data.xlsx', index_col='user_id', sheet_name='page2') 
df = pd.read_excel('data_frame/user_data.xlsx') 
print(df)

# その他
# df = pd.read_csv('user_data.cvs')
# df = pd.read_json('user_data.json')
# df = pd.read_html('user_data.html')

# Jupyter LabやGoogle Colabratoryのほうが扱いやすい