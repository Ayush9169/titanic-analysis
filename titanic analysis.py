import numpy as np
import pandas as pd
dataset = pd.read_excel("C:\\Users\\hp\\Downloads\\titanic3.xls")
dataset.boat = dataset.boat.fillna(0)
dataset.body = dataset.body.fillna(0)
observed=[]
for i in range(0,1309):
    if (dataset.boat[i] is 0):
        observed.append(0)
    if (dataset.boat[i] is not 0):
        observed.append(1)
pred=0
for i in range(0,1309):
    if dataset.survived[i] == observed[i]:
        pred+= 1
    else:
        pass
print(pred)
analysis =(int(pred)*100)//1309
print(analysis)