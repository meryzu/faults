import pandas as pd
from Process import Prepare
from Scenaries import Scene

extention=5 #Number of time steps to be taken

df=pd.read_csv('../data/FallasJunioNew.csv') #read data from csv file
data=Prepare.prepare(df,16,20,24,28) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing

#train=data.sample(frac=0.8,random_state=200)
#test=data.drop(train.index)


z=Scene.scene(data,'4H','Time')#H: horas, min: minutos, 24h es x dia

# to combine X1
scenary_x1_1=Scene.scene1(z,extention,28)

scenary_x1_2=Scene.scene2(z,extention,16,28)
scenary_x1_3=Scene.scene2(z,extention,20,28)
scenary_x1_4=Scene.scene2(z,extention,24,28)

scenary_x1_5=Scene.scene3(z,extention,16,20,28)
scenary_x1_6=Scene.scene3(z,extention,16,24,28)
scenary_x1_7=Scene.scene3(z,extention,20,24,28)

scenary_x1_8=Scene.scene4(z,extention,16,20,24,28)

scenary_x1_1.to_csv('../data/datascenary_x1_1.csv',index=False)
scenary_x1_2.to_csv('../data/datascenary_x1_2.csv',index=False)
scenary_x1_3.to_csv('../data/datascenary_x1_3.csv',index=False)
scenary_x1_4.to_csv('../data/datascenary_x1_4.csv',index=False)
scenary_x1_5.to_csv('../data/datascenary_x1_5.csv',index=False)
scenary_x1_6.to_csv('../data/datascenary_x1_6.csv',index=False)
scenary_x1_7.to_csv('../data/datascenary_x1_7.csv',index=False)
scenary_x1_8.to_csv('../data/datascenary_x1_8.csv',index=False)


###### to combine X2
#data=Prepare.prepare(df,20,24,28,16) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing

#train=data.sample(frac=0.8,random_state=200)
#test=data.drop(train.index)


#z=Scene.scene(train,'1H','Time')#H: horas, min: minutos

# to combine x2
scenary_x2_1=Scene.scene1(z,extention,16)

scenary_x2_2=Scene.scene2(z,extention,20,16)
scenary_x2_3=Scene.scene2(z,extention,24,16)
scenary_x2_4=Scene.scene2(z,extention,28,16)

scenary_x2_5=Scene.scene3(z,extention,20,24,16)
scenary_x2_6=Scene.scene3(z,extention,24,28,16)
scenary_x2_7=Scene.scene3(z,extention,20,28,16)

scenary_x2_8=Scene.scene4(z,extention,20,24,28,16)

scenary_x2_1.to_csv('../data/datascenary_x2_1.csv',index=False)
scenary_x2_2.to_csv('../data/datascenary_x2_2.csv',index=False)
scenary_x2_3.to_csv('../data/datascenary_x2_3.csv',index=False)
scenary_x2_4.to_csv('../data/datascenary_x2_4.csv',index=False)
scenary_x2_5.to_csv('../data/datascenary_x2_5.csv',index=False)
scenary_x2_6.to_csv('../data/datascenary_x2_6.csv',index=False)
scenary_x2_7.to_csv('../data/datascenary_x2_7.csv',index=False)
scenary_x2_8.to_csv('../data/datascenary_x2_8.csv',index=False)

df=pd.read_csv('../data/FallasJunioNew.csv') #read data from csv file
data=Prepare.prepare(df,16,20,24,28) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing


###### to combine X3
data=Prepare.prepare(df,16,24,28,20) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing

#z=Scene.scene(train,'1H','Time')#H: horas, min: minutos

# to combine x3
scenary_x3_1=Scene.scene1(z,extention,20)
scenary_x3_2=Scene.scene2(z,extention,16,20)
scenary_x3_3=Scene.scene2(z,extention,24,20)
scenary_x3_4=Scene.scene2(z,extention,28,20)

scenary_x3_5=Scene.scene3(z,extention,16,24,20)
scenary_x3_6=Scene.scene3(z,extention,16,28,20)
scenary_x3_7=Scene.scene3(z,extention,24,28,20)

scenary_x3_8=Scene.scene4(z,extention,16,24,28,20)

scenary_x3_1.to_csv('../data/datascenary_x3_1.csv',index=False)
scenary_x3_2.to_csv('../data/datascenary_x3_2.csv',index=False)
scenary_x3_3.to_csv('../data/datascenary_x3_3.csv',index=False)
scenary_x3_4.to_csv('../data/datascenary_x3_4.csv',index=False)
scenary_x3_5.to_csv('../data/datascenary_x3_5.csv',index=False)
scenary_x3_6.to_csv('../data/datascenary_x3_6.csv',index=False)
scenary_x3_7.to_csv('../data/datascenary_x3_7.csv',index=False)
scenary_x3_8.to_csv('../data/datascenary_x3_8.csv',index=False)


###### to combine X4
#data=Prepare.prepare(df,16,24,28,20) #posicion de la falla en el array de fallas (failureCode)

#Incluir con data las dos tablas de training y testing


#z=Scene.scene(train,'1H','Time')#H: horas, min: minutos

# to combine x4
scenary_x4_1=Scene.scene1(z,extention,24)
scenary_x4_2=Scene.scene2(z,extention,16,24)
scenary_x4_3=Scene.scene2(z,extention,20,24)
scenary_x4_4=Scene.scene2(z,extention,28,24)

scenary_x4_5=Scene.scene3(z,extention,16,20,24)
scenary_x4_6=Scene.scene3(z,extention,16,28,24)
scenary_x4_7=Scene.scene3(z,extention,20,28,24)

scenary_x4_8=Scene.scene4(z,extention,16,20,28,24)

scenary_x4_1.to_csv('../data/datascenary_x4_1.csv',index=False)
scenary_x4_2.to_csv('../data/datascenary_x4_2.csv',index=False)
scenary_x4_3.to_csv('../data/datascenary_x4_3.csv',index=False)
scenary_x4_4.to_csv('../data/datascenary_x4_4.csv',index=False)
scenary_x4_5.to_csv('../data/datascenary_x4_5.csv',index=False)
scenary_x4_6.to_csv('../data/datascenary_x4_6.csv',index=False)
scenary_x4_7.to_csv('../data/datascenary_x4_7.csv',index=False)
scenary_x4_8.to_csv('../data/datascenary_x4_8.csv',index=False)

