import pandas as pd
from failureCode import Code
import numpy as np

class Scene():
    def scene(data,period,column):
        data1=data.resample(period, on=column).sum()
        data1['Timex']=data1.index.time
        data1=data1.groupby('Timex').mean()
        return data1

    def scene1(data,b,x4): # b: El numero de horas o minutos que toma hacia atras. Solo out of cash 4.
        a=len(data.index)
        scene=pd.DataFrame(index=data.index[b:a],columns=range(0,b+1))
        for i in range (0,a-b):
            temarr = data.ix[data.index[i:i + b], Code.code(x4)].values
            temarr = np.append(temarr,['0'])
            temparr1 = np.transpose(temarr)
            scene.ix[scene.index[i]] = temparr1
        scene.ix[scene.index[0:a - b], b] = data.ix[data.index[b:a], Code.code(x4)]
        return scene

    def scene2(data, b, x1, x4):  # b: El numero de horas o minutos que toma hacia atras. Out of cash 4 con una variable.
        a = len(data.index)
        scene = pd.DataFrame(index=data.index[b:a], columns=range(0, b+2))
        for i in range(0, a - b):
            temarr=data.ix[data.index[i:i + b], Code.code(x1)].values
            temarr = np.append(temarr,['0'])
            temarr = np.append(temarr, ['0'])
            temparr1 = np.transpose(temarr)
            scene.ix[scene.index[i]] = temparr1
        scene.ix[scene.index[0:a - b], b] = data.ix[data.index[b:a], Code.code(x1)]
        scene.ix[scene.index[0:a-b],b+1]=data.ix[data.index[b:a],Code.code(x4)]
        return scene

    def scene3(data, b, x1,x2, x4):  # b: El numero de horas o minutos que toma hacia atras
        a = len(data.index)
        scene = pd.DataFrame(index=data.index[b:a], columns=range(0, 2*b+3))
        for i in range(0, a - b):
            temarr = data.ix[data.index[i:i + b], Code.code(x1)].values
            temarr2=data.ix[data.index[i:i + b], Code.code(x2)].values
            temparr1 = np.ravel(np.column_stack((temarr,temarr2)))#intercalacion de variables
            temparr1 = np.append(temparr1, ['0'])
            temparr1 = np.append(temparr1, ['0'])
            temparr1 = np.append(temparr1, ['0'])
            temparr2 = np.transpose(temparr1)
            scene.ix[scene.index[i]] = temparr2
        scene.ix[scene.index[0:a - b], 2 * b] = data.ix[data.index[b:a], Code.code(x1)]
        scene.ix[scene.index[0:a - b], 2 * b+1] = data.ix[data.index[b:a], Code.code(x2)]
        scene.ix[scene.index[0:a - b], 2*b+2] = data.ix[data.index[b:a], Code.code(x4)]
        return scene

    def scene4(data, b, x1, x2,x3, x4):  # b: El numero de horas o minutos que toma hacia atras
        a = len(data.index)
        scene = pd.DataFrame(index=data.index[b:a], columns=range(0, 3 * b+4))
        for i in range(0, a - b):
            temarr = data.ix[data.index[i:i + b], Code.code(x1)].values
            temarr2 = data.ix[data.index[i:i + b], Code.code(x2)].values
            temarr3=data.ix[data.index[i:i + b], Code.code(x3)].values
            temparr1 =np.ravel(np.column_stack((temarr,temarr2,temarr3)))
            temparr1 = np.append(temparr1, ['0'])
            temparr1 = np.append(temparr1, ['0'])
            temparr1 = np.append(temparr1, ['0'])
            temparr1 = np.append(temparr1, ['0'])
            temparr2 = np.transpose(temparr1)
            scene.ix[scene.index[i]] = temparr2
        scene.ix[scene.index[0:a - b], 3 * b] = data.ix[data.index[b:a], Code.code(x1)]
        scene.ix[scene.index[0:a - b], 3 * b+1] = data.ix[data.index[b:a], Code.code(x2)]
        scene.ix[scene.index[0:a - b], 3 * b+2] = data.ix[data.index[b:a], Code.code(x3)]
        scene.ix[scene.index[0:a - b], 3 * b+3] = data.ix[data.index[b:a], Code.code(x4)]
        return scene

