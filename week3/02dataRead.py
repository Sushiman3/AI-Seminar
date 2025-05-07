import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

def mSurviv(df):
    male = df[df['Sex'] == 'male']
    array = male.values
    res = np.mean(array[:,1])
    return res

def fSurviv(df):
    female = df[df['Sex'] == 'female']
    array = female.values
    res = np.mean(array[:,1])
    return res

# 男性の生存率を求める
male_survival_rate = mSurviv(df)

# 女性の生存率を求める
female_survival_rate = fSurviv(df)


print(f"男性の生存率: {male_survival_rate:.3f}")
print(f"女性の生存率: {female_survival_rate:.3f}")