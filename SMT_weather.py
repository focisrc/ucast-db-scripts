import os
import numpy as np ,pandas as pd , matplotlib.pyplot as plt
import scipy as sci
from scipy import signal
import os

os.chdir("C:/Users/phaniv/Dropbox/EHT Weather CSV Files")
print(os.getcwd())
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
 
def process_month(tau,df):
    c = df['median'].le(tau)
    # The main problem with this approach is it breaks when it encounters discontinuous
    # data  Such as 2:59am , 3:00 am and 10:00 pm as three consecutive rows. The
    # Average number of nows becomes impossibly high as a result). In other words, if a morning and the next evening have similar opacities,
    # this just adds it to the time instead of resetting it. 
    # TODO: Need to fix it by some version of groupby day_select() function
    s = c.ne(c.shift()).cumsum()
    u = (s.where(c&s.duplicated(keep=False)).groupby(df['site'],sort=False)
                                            .agg(['count','nunique','std']))
    
    out = (u.join(u['count'].div(u['nunique']).rename("Avg_duration")).reset_index().drop("count",1).rename(columns={"nunique":"Count"}))
    out.Avg_duration=out.Avg_duration.apply(lambda x: x*24/288)
    out["tau"]=tau
    out["std"]=out["std"].apply(lambda x: x*24/288)
    return (out)



def calculate(df,site):
    taus=np.arange(0,1,0.01)
    ldf=[process_month(tau,df) for tau in taus]
    return ldf

def plot(ls):
    e=[float(out["std"]) for out in ls[1:]]
    print(e)
    x=[float(out["tau"]) for out in ls[1:]]
    y=[float(out["Avg_duration"]) for out in ls[1:]]
    plt.xlabel("Tau")
    plt.ylabel("Time(T< Tau) in hours")
    plt.title("Distribution plot for",ls[0].site[0])
    plt.xlim(0,0.5)
    plt.ylim(0,15)
    plt.errorbar(x, y, yerr = e)
    plt.show()

def rolling_median(df):
    # 12 means 60 minutes as each row is 5 mins
    df['median']= df['tau'].rolling(pd.Timedelta('60 min')).median()

    return df

# def day_select(defgr):
#   # returns list of dataframes grouped by date
#     result = [group[1] for group in defgr.groupby(df.index.date)]
#     return result


janwk1,jan=load(1)
ls=calculate(janwk1)
med1jan = rolling_median(janwk1)
plot(calculate(med1jan))


