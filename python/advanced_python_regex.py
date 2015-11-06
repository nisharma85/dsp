import pandas as pd
import numpy as np
from string import replace
import os

os.getcwd()
os.chdir('C:/Users/shani16/Documents/Python_dsp')

data=pd.read_csv('faculty.csv')

data[:3]


data = data.rename(columns=lambda x: x.strip())

data.columns



data['title'] = data['title'].apply(lambda x: x.split(' ')[0])

title_count=data.groupby('title')._count()


degree= pd.melt(pd.DataFrame(list(data.degree.str.split())))
degree['value'] = degree.value.apply(lambda x: str(x).strip())
degree['value'] = degree['value'].str.replace('.', '')
degree =  degree[(degree['value'] !="None")]
degree =  degree[(degree['value'] !="0")]

g = degree.groupby('value').count()

g.count()

email=[]
email.append(data.email)
print email

data['name_email'], data['domain'] = zip(*data['email'].apply(lambda x: x.split('@', 1)))

email=data.groupby('domain')._count()

email_unique=np.unique(data[['domain']])

print email_unique
