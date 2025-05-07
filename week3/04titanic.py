import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

def classSurv(df):
    x = df[df['Pclass'] == 3]
    array = x.values
    res = np.mean(array[:,1])
    return res

print(classSurv(df))