import pandas as pd
from Process import Prepare
from Scenaries import Scene


df=pd.read_csv('../data/FallasJunio.csv') #read data from csv file

data=Prepare.prepare(df,16,20,24,28) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing

extention=5 #Number of time steps to be taken

z=Scene.scene(data,'1H','Time')#H: horas, min: minutos

scenary1=Scene.scene1(z,extention,28)
scenary2=Scene.scene2(z,extention,16,28)
scenary3=Scene.scene2(z,extention,20,28)
scenary4=Scene.scene2(z,extention,24,28)

scenary5=Scene.scene3(z,extention,16,20,28)
scenary6=Scene.scene3(z,extention,20,24,28)
scenary7=Scene.scene3(z,extention,16,24,28)

scenary7=Scene.scene4(z,extention,16,20,24,28)

print(scenary1)
print(scenary2)
print(scenary3)
print(scenary4)
print(scenary5)
print(scenary6)
print(scenary7)
scenary1.to_csv('../data/datascenary1')
scenary2.to_csv('../data/datascenary2')
scenary3.to_csv('../data/datascenary3')
scenary4.to_csv('../data/datascenary4')
scenary5.to_csv('../data/datascenary5')
scenary6.to_csv('../data/datascenary6')
scenary7.to_csv('../data/datascenary7')
#z.to_csv('dataTemp.csv')