import numpy as np

data_2d = np.array([
    [1,10],
    [2,20],
    [3,30]
])

def standardize(data):
    for i in range(2):
        mean = np.mean(data[:, i])
        std = np.std(data[:, i])
        data[:, i] = (data[:, i] - mean) / std
    return data


standardized_data_2d = standardize(data_2d)

print("元の2次元データ:\n", data_2d)
print("標準化された2次元データ（列ごと）:\n", standardized_data_2d)