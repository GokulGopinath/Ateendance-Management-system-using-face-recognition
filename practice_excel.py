import pandas as pd
from datetime import date,timedelta 



# data=[['23-01-2020',0,1]]
df=pd.read_excel('attendance.xlsx')


df['date']= pd.to_datetime(df['date'])
df.set_index('date',inplace=True)


# df['rahul']=0
# df['ajay']=0
d=pd.to_datetime(date.today()+timedelta(1))
# df.loc[d,'rahul']=1
df.loc[d]=0
print(df.index.isin([d]).sum())

# print(df.head())
# df['rahul']=0
# df.to_excel("attendance.xlsx")