import pandas as pd

data1 = {
    'id': ['100', '101', '102', '103', '104', '106', '108', '110', '111','113'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru','Mitsuo']
}
df1 = pd.DataFrame(data1)

data2 = {
    'id': ['117', '118', '119', '120', '125'],
    'city': ['Chiba', 'Kanagawa', 'Tokyo', 'Fukuoka', 'Okinawa'],
    'birth_year': [1990, 1989, 1992, 1997, 1982],
    'name': ['Suguru', 'Kouichi', 'Satochi', 'Yukie', 'Akari']
}
df2 = pd.DataFrame(data2)

data3 = {
    'id': ['100', '101', '102', '105', '107'],
    'math': [50, 43, 33, 76, 98],
    'english': [90, 30, 20, 50, 30],
    'sex': ['M','F','F','M','M'],
    'index_num': [0, 1, 2, 3, 4]
}
df3 = pd.DataFrame(data3)

data = [df1, df2]

for i in data:
    print(i)
    print("\n")

merged_df = pd.merge(df1, df2, how='outer')
print("Merged DataFrame:")
print(merged_df)