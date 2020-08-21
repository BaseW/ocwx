import pandas as pd

user_list = [i for i in range(11)]
kokugo_list = [i for i in range(11, 22)]
df = pd.DataFrame({'user':user_list, 'kokugo':kokugo_list})
print(df)
