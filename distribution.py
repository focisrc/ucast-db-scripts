def load(month):
    df = pd.read_csv(filename, error_bad_lines=False,header=0)
    df.index=pd.to_datetime(df.index)
    # Filter by hours
    ndf=df.between_time('22:00','03:00')
    monthdf =ndf[ndf.index.month == month]
    monthdf.index=pd.to_datetime(monthdf.index)
    return monthdf
 
def process_month(tau,df):
    c = df['tau'].le(tau)
    s = c.ne(c.shift()).cumsum()
    u = (s.where(c&s.duplicated(keep=False)).groupby(df['name'],sort=False)
                                            .agg(['count','nunique']))
    out = (u.join(u['count'].div(u['nunique']).rename("Avg_duration")).reset_index()
        .drop("count",1).rename(columns={"nunique":"Count"}))
    
    return out



  taus=np.arange(0,1,0.05)
  ldf=[foo(tau,jan) for tau in taus]
