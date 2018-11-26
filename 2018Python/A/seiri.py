import pandas as pd
import csv
import os

path = './data/'
files = []

for x in os.listdir(path):
    if os.path.isfile(path + x):
        x=x.replace('.csv','')
        files.append(x)

data_list = pd.DataFrame(columns=['name'])

for (file0, i) in zip(files, range(len(files))):
    test_data = pd.read_csv('./data/'+file0+'.csv', dtype='object')
    test_data = test_data[['name', 'data']]
    test_data = test_data.rename(columns={'data': file0})
    data_list = pd.merge(data_list, test_data, right_on='name', left_on='name', how='outer')

    

data_list = data_list.set_index('name')
data_list.to_csv('./data/merge/merge_data.csv')
