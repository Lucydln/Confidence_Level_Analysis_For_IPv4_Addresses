import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 30) # set so can see all columns of the DataFrame
import matplotlib.pyplot as plt
import csv
from itertools import zip_longest


df = pd.read_csv('per ip daily user num.csv') #reading data

xrealip = df['xrealip'].unique()
print(f'Total number of distinct ip: {len(xrealip)}')

d1 = {}
for i in xrealip:
    d1[i] = df[df['xrealip'] == i]['daily_user_num']


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

bs_replicates_user = {}
for i in d1:
    bs_replicates_user[i] = draw_bs_replicates(d1[i],np.mean,1500)

# Plot the PDF for bootstrap replicates as histogram
for i in bs_replicates_user:
    # print(i)
    plt.hist(bs_replicates_user[i],bins=30, density = True)
    # Showing the related percentiles
    plt.axvline(x=np.percentile(bs_replicates_user[i],[50]), ymin=0, ymax=1,label='50th percentile',c='y')
    # plt.axvline(x=np.percentile(bs_replicates_user[i],[97.5]), ymin=0, ymax=1,label='97.5th percentile',c='r')
    plt.xlabel("User Number")
    plt.ylabel("PDF")
    plt.title("Probability Density Function")
    plt.legend()
    plt.show()
    # break  # for testing purposes, only plot one account


# Get the corresponding values of 2.5th
conf_interval = {}
for i in bs_replicates_user:
    conf_interval[i] = np.percentile(bs_replicates_user[i], 50)
    # Print the interval
    # print("The confidence interval: >",conf_interval[i])
    # break

conf_interval_list = []
for i in conf_interval:
    conf_interval_list.append(conf_interval[i])
# print(conf_interval_list)

conf_interval_percentile = np.percentile(conf_interval_list, 2.5)
# print(conf_interval_percentile)


ip_filtered = []
for i in xrealip:
    if conf_interval[i] > conf_interval_percentile:
        ip_filtered.append(i)
# print(ip_filtered)
# print(len(ip_filtered))








df1 = pd.read_csv('per ip daily ip usage.csv')
 
xrealip1 = df1['xrealip'].unique()
# print(len(xrealip1))

d2 = {}
for i in xrealip1:
    d2[i] = df1[df1['xrealip'] == i]['daily_ip_usage']

bs_replicates_ip = {}
for i in d2: 
    bs_replicates_ip[i] = draw_bs_replicates(d2[i],np.mean,1500)

# Plot the PDF for bootstrap replicates as histogram
for i in bs_replicates_ip:
    plt.hist(bs_replicates_ip[i],bins=30, density = True)
    # Showing the related percentiles
    plt.axvline(x=np.percentile(bs_replicates_ip[i],[2.5]), ymin=0, ymax=1,label='2.5th percentile',c='y')
    # plt.axvline(x=np.percentile(bs_replicates_user[i],[97.5]), ymin=0, ymax=1,label='97.5th percentile',c='r')
    # plt.xlabel("IP Usage")
    # plt.ylabel("PDF")
    # plt.title("Probability Density Function")
    # plt.legend()
    # plt.show()
    # break  # for testing purposes, only plot one account


# Get the corresponding values of 2.5th
conf_interval1 = {}
for i in bs_replicates_ip:
    conf_interval1[i] = np.percentile(bs_replicates_ip[i], 50)
    # Print the interval
    # print("The confidence interval: >", conf_interval1[i])
    # break


conf_interval_list1 = []
for i in conf_interval1:
    conf_interval_list1.append(conf_interval1[i])
# print(conf_interval_list1)

conf_interval_percentile1 = np.percentile(conf_interval_list1, 2.5)
# print(conf_interval_percentile1)



ip_filtered1 = []
for i in xrealip1:
    if conf_interval1[i] > conf_interval_percentile1:
        ip_filtered1.append(i)
# print(ip_filtered1)
# print(len(ip_filtered1))



ip_filtered_final = []
for i in xrealip:
    if i in ip_filtered1 and i in ip_filtered:
        ip_filtered_final.append(i)

print(f'Total number of trusted ip: {len(ip_filtered_final)}')

ip_excluded = []
for i in xrealip:
    if i not in ip_filtered_final:
        ip_excluded.append(i)

print(f'Total number of excluded ip: {len(ip_excluded)}')

d = [ip_filtered_final, ip_excluded]
with open('per ip filtered and excluded.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['ip_filtered', 'ip_excluded'])
    for values in zip_longest(*d):
        writer.writerow(values)






