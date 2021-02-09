import pandas as pd
data=[['23-01-2020',0,1]]
df=pd.DataFrame(data,columns=['date','ramesh','raj'])
df.set_index('date',inplace=True)
df['rahul']=0
df.to_excel("attendance.xlsx")