import os

import pandas as pd

data_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(data_dir, 'user_data.xlsx')
df = pd.read_excel(data_path)
# df = pd.read_csv(data_path)
# df = pd.read_json(data_path)
# df = pd.read_html(data_path)

print(df)

