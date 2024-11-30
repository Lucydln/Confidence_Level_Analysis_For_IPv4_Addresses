import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 30) # set so can see all columns of the DataFrame
import matplotlib.pyplot as plt
import csv
from itertools import zip_longest


df = pd.read_csv('per acct per ip daily user num.csv') # reading data

acct = df['account_id'].unique()
ip_df = df['xrealip'].unique()
print(f'Total number of distinct ip: {len(ip_df)}')

d1 = {}
for i in acct:
    d1[i] = pd.DataFrame(zip(df[df['account_id'] == i]['xrealip'], df[df['account_id'] == i]['daily_user_num']), columns=['xrealip', 'user_number'])

def draw_bs_replicates(data,func,size):
    """creates a bootstrap sample, computes replicates and returns replicates array"""
    # Create an empty array to store replicates
    bs_replicates = np.empty(size)
    
    # Create bootstrap replicates as much as size
    for i in range(size):
        # Create a bootstrap sample
        bs_sample = np.random.choice(data,size=len(data))
        # Get bootstrap replicate and append to bs_replicates
        bs_replicates[i] = func(bs_sample)
    
    return bs_replicates

conf_interval_percentile = {}
ip_filtered = {}

for i in d1:
    confidence_interval = {}
    confidence_interval_list = []
    for j in d1[i]['xrealip'].unique(): 
        temp = draw_bs_replicates(d1[i][d1[i]['xrealip'] == j]['user_number'],np.mean,1500)
        confidence_interval[j] = np.percentile(temp, 50)
    for m in confidence_interval.values():
        confidence_interval_list.append(m)
    # temp = draw_bs_replicates(confidence_interval_list, np.mean, 150)
    conf_interval_percentile[i] = np.percentile(confidence_interval_list, 2.5)
    ip_filtered_list = []
    for m,n in confidence_interval.items():
        if n > conf_interval_percentile[i]:
            ip_filtered_list.append(m)
    ip_filtered[i] = ip_filtered_list
    # print(ip_filtered[i])
    # break






df1 = pd.read_csv('per acct per ip daily ip usage.csv')

acct1 = df1['account_id'].unique()

d2 = {}
for i in acct1:
    d2[i] = pd.DataFrame(zip(df1[df1['account_id'] == i]['xrealip'], df1[df1['account_id'] == i]['daily_ip_usage']), columns=['xrealip', 'ip_usage'])



conf_interval_percentile1 = {}
ip_filtered1 = {}

for i in d2:
    confidence_interval1 = {}
    confidence_interval_list1 = []
    for j in d2[i]['xrealip'].unique(): 
        temp = draw_bs_replicates(d2[i][d2[i]['xrealip'] == j]['ip_usage'],np.mean,1500)
        confidence_interval1[j] = np.percentile(temp, 50)
    for m in confidence_interval1.values():
        confidence_interval_list1.append(m)
    # temp = draw_bs_replicates(confidence_interval_list1, np.mean, 150)
    conf_interval_percentile1[i] = np.percentile(confidence_interval_list1, 2.5)
    ip_filtered_list1 = []
    for m,n in confidence_interval1.items():
        if n > conf_interval_percentile1[i]:
            ip_filtered_list1.append(m)
    ip_filtered1[i] = ip_filtered_list1
    # print(ip_filtered1[i])
    # break



ip_filtered_final = {}
for i in acct:
    if i in ip_filtered and i in ip_filtered1:
        ip_list = list(set(ip_filtered[i] + ip_filtered1[i]))
        temp = pd.DataFrame(ip_list, columns=['xrealip'])
        ip_filtered_final[i] = temp
        ip_filtered_final[i].insert(0, 'account_id', i)
      


with open('per_acct_per_ip_filtered.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames= ['account_id', 'xrealip'])
    writer.writeheader()
    for key in ip_filtered_final.keys():
        ip_filtered_final[key] = ip_filtered_final[key].to_dict('records')
        writer.writerows(ip_filtered_final[key])


filtered_df = pd.read_csv('per_acct_per_ip_filtered.csv')
filtered_ip = filtered_df['xrealip'].unique()
filtered_ip_list = []
for i in filtered_ip:
    filtered_ip_list.append(i)
ip_excluded = []
for i in ip_df:
    if i not in filtered_ip_list:
        ip_excluded.append(i)
# print(filtered_ip_list)
print(f'Total number of trusted ip: {len(filtered_ip_list)}')
# print(ip_excluded)
print(f'Total number of excluded ip: {len(ip_excluded)}')

d = [filtered_ip_list, ip_excluded]
with open("per acct per ip filtered and excluded.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(['ip_filtered', 'ip_excluded'])
    for values in zip_longest(*d):
        writer.writerow(values)
