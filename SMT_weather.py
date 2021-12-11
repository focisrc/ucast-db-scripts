import os
import numpy as np ,pandas as pd , matplotlib.pyplot as plt
import scipy as sci
from scipy import signal
import os
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
    c = df['median'].le(tau)
    lengths=[]
    for k, g in groupby(c.values):
            g = list(g)
            if k==1:
                lengths.append(len(g))
    return (np.mean(lengths),np.std(lengths),len(df))


def get_split_locs(df):
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



week1df,monthdf=load(1)
loc_list=get_split_locs(week1df)
df_list=split_df(loc_list,week1df)
del df_list[-1]
for day in range(0,len(df_list)):
    rolling_median(df_list[day])

taus=np.arange(0,1.1,0.1)
stats=dict()
for tau in taus:
    stats[tau]=[]
for day in df_list:
    for tau in taus:
        stats[tau].append((day_stats(tau,day)))
dict_to_df = [(k, *t) for k, v in stats.items() for t in v]
df = pd.DataFrame(dict_to_df, columns=['tau','mean','sd',"length"]).dropna()
means=[]
sds=[]
for tau in taus:
    df2=df[df["tau"]==tau]
    weighted_stats = DescrStatsW(df2["mean"].values, weights=df2["length"].values, ddof=0)
    means.append(weighted_stats.mean*24/288)
    sds.append(weighted_stats.std*24/288)
plot(taus,means,sds)
