import pandas as pd
from failureCode import Code

class Prepare():
    def prepare(data,x1,x2,x3,x4):

        data1=data.drop(['NombreATMOCM','Marca','Modelo','Atmkey','Anio','Mes','Dia','Hora','Minutos','FaultId','StartTime_Timestamp','EndTime_Timestamp','Type'],axis=1)

        temptime=pd.DataFrame({'year':data['Anio'],'month':data['Mes'],'day':data['Dia'],'hour':data['Hora'],'minute':data['Minutos']})

        temptime=pd.to_datetime(temptime)

        data1['Time']=temptime

        data1=data1[(data1.FaultDesc[:]==Code.code(x1))
                    |(data1.FaultDesc[:]==Code.code(x2))
                    |(data1.FaultDesc[:]==Code.code(x3))
                    |(data1.FaultDesc[:] == Code.code(x4))]

        data1[Code.code(x1)]=data1.FaultDesc
        data1[Code.code(x1)].replace(to_replace=[Code.code(x1)],value=1,inplace=True)
        data1[Code.code(x1)].replace(to_replace=[Code.code(x2),Code.code(x3),Code.code(x4)], value=0, inplace=True)

        data1[Code.code(x2)] = data1.FaultDesc
        data1[Code.code(x2)].replace(to_replace=[Code.code(x2)], value=1, inplace=True)
        data1[Code.code(x2)].replace(to_replace=[Code.code(x1), Code.code(x3), Code.code(x4)], value=0, inplace=True)

        data1[Code.code(x3)] = data1.FaultDesc
        data1[Code.code(x3)].replace(to_replace=[Code.code(x3)], value=1, inplace=True)
        data1[Code.code(x3)].replace(to_replace=[Code.code(x2), Code.code(x1), Code.code(x4)], value=0, inplace=True)

        data1[Code.code(x4)] = data1.FaultDesc
        data1[Code.code(x4)].replace(to_replace=[Code.code(x4)], value=1, inplace=True)
        data1[Code.code(x4)].replace(to_replace=[Code.code(x2), Code.code(x3), Code.code(x1)], value=0, inplace=True)

        data1.drop(['FaultDesc'], axis=1,inplace=True)

        return data1
