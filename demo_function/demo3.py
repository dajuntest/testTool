import csv

import numpy as np
import pandas as pd



# with open('saved_data.csv', 'a', encoding='utf-8', newline='') as f:
#     myWrite = csv.writer(f)
#     myWrite.writerow(['1', 2, 3])
#
#
# with open('saved_data.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for i in reader:
#         print(i)

df = pd.DataFrame(pd.read_csv('demo.csv', delimiter=',', encoding='utf-8'))
# df.columns = ['element', 'local_type', 'local_value']

# rows = df[0:3]
# print(rows)
# df['产品'] = df['产品'].append(pd.Series('123'), ignore_index=True)
# print(cols.values)
# series = {'页面': '123'}
# df = df.append(series, ignore_index=True)
print(df)
# print(cols.index)
# print(df[df['产品'].isin(['ser'])])
# print(len(df[df == 'ser']))
# print(df['产品'])
# df.to_csv('saved_data.csv')
# print(df)
# print('lks' in cols.values)

# dates = pd.date_range('20130101', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list(['你', '士大夫', '士大夫', '定位']))
# print(df)


