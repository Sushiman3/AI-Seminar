import pandas as pd
import numpy as np

df = pd.read_csv('./titanic.csv')

def survival(df,sex):
    male = df[df['Sex'] == sex]
    array = male.values
    res = np.mean(array[:,1])
    return res


# 男性の生存率を求める
male_survival_rate = survival(df,'male')

# 女性の生存率を求める
female_survival_rate = survival(df,'female')


print(f"男性の生存率: {male_survival_rate:.3f}")
print(f"女性の生存率: {female_survival_rate:.3f}")
