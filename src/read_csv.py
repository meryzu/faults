#from pandas import pandas

#def print_data():
#df = pandas.read_csv('../data/FallasJunio.csv')
#dfhours = df.groupby(('Hora','Marca')).agg({'Marca':['count']})
#print(df)

import pandas as pd
from Process import Prepare
from Scenaries import Scene


df=pd.read_csv('../data/FallasJunio.csv') #read data from csv file

data=Prepare.prepare(df,16,20,24,28) #posicion de la falla en el array de fallas (failureCode)
train=data.sample(frac=0.8,random_state=200)
test=data.drop(train.index)

print(test.head)
#print test.head()
