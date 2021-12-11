import os
import numpy as np ,pandas as pd , matplotlib.pyplot as plt
import scipy as sci
from scipy import signal
import os
from itertools import groupby
from statsmodels.stats.weightstats import DescrStatsW

filename="SMT_data_edit.csv"

def load(month):
  # month: integer representing month of year
    df = pd.read_csv(filename, error_bad_lines=False,header=0,usecols = ['dateStart','tau'])
    df.index=pd.to_datetime(df.index)
    # Filter by hours 8 pm to 3 am
    ndf=df.between_time('20:00','03:00')
    # January
    monthdf =ndf[ndf.index.month == month]
    # First week
    week1df = monthdf[monthdf.index.isocalendar().week==1]
    
    # monthdf.index=pd.to_datetime(monthdf.index)
    # monthdf.site="SMT"
    week1df["site"]="SMT"
    monthdf["site"]="SMT"
    return week1df,monthdf
 
def day_stats(tau,df):
    # Custom function to solve this sample problem
    # Threshold : 5
    # input: [0,1,3,4,5,5.1,5.1,0,3,9] 
    # output: [5,2]
    # Process: Gets all the lengths of consecutive numbers less than threshold
    # We need this for the Tau vs time p
    # Returns the mean, standard deviation and length of observing period to account for discrepancies in number of observations
    c = df['median'].le(tau)
    lengths=[]
    for k, g in groupby(c.values):
            g = list(g)
            if k==1:
                lengths.append(len(g))
    return (np.mean(lengths),np.std(lengths),len(df))


def get_split_locs(df):
  # This gets the index values for dataframe to be split by observation night
    compare_dt= list(df.index)
    del compare_dt[0]
    i=0
    split_list=[]
    for past,present in zip(a,janwk1.index):
        if past-present > pd.Timedelta("1 hour"):
            # print(past,present,past-present)
            split_list.append(i)
        i+=1
    return split_list

def split_df(locs,df):
    # This splits the dataframe with the loc values from get_split_locs
    ldf=[]
    ldf.append(df.iloc[:locs[0],:])
    print(ldf)
    for i in range(len(locs)-1):
        ldf.append(df.iloc[locs[i]:locs[i+1],:])
    ldf.append(df.iloc[locs[0]:,:])
    return ldf


def plot(x,y,e):
    plt.xlabel("Tau")
    plt.ylabel("Time(T< Tau) in hours")
    plt.xlim(0,1)
    plt.ylim(0,15)
    plt.errorbar(x, y, yerr = e)
    plt.show()

def rolling_median(df):
    # 12 means 60 minutes as each row is 5 mins
    df['median']= df['tau'].rolling(pd.Timedelta('15 min')).median()

    return df


# Loading the first week of January and the whole month
# We only use week1df in the rest of the script , feel free to play around with monthdf ( in this case january df)
week1df,monthdf=load(1)
# We split the dataframe into a list of dataframes with each observing period 
loc_list=get_split_locs(week1df)
df_list=split_df(loc_list,week1df)

# Deleting the final df (as it is the whole df and fixes an off by 1 error )
del df_list[-1]
# For each observing period 10pm-3 am in this case, we apply a rolling median filter of 15 minutes
for day in range(0,len(df_list)):
    rolling_median(df_list[day])



# Tau values (Accuracy can be improved by changed 0.1 to 0.01)
taus=np.arange(0,1.1,0.1)
# Making a dictionary of aggregated statistics for each day
stats=dict()
for tau in taus:
    stats[tau]=[]
for day in df_list:
    for tau in taus:
        stats[tau].append((day_stats(tau,day)))
# converting the dictionary to a dataframe
dict_to_df = [(k, *t) for k, v in stats.items() for t in v]
df = pd.DataFrame(dict_to_df, columns=['tau','mean','sd',"length"]).dropna()

# TODO: Play around with ddof

# Getiing weighted statistics (Some days do not have records for the whole 5 hours we need,so I weigh their mean with df["length"])
# TODO: Consider if weifghted averages are even needed
means=[]
sds=[]
for tau in taus:
    df2=df[df["tau"]==tau]
    weighted_stats = DescrStatsW(df2["mean"].values, weights=df2["length"].values, ddof=0)
    # We divide it by 12 as data is collected every 5 minutes ( 12*5=60 min = 1hour)
    means.append(weighted_stats.mean/12)
    sds.append(weighted_stats.std/12)
plot(taus,means,sds)
