import pandas as pd
import random
import math

user_list = [i for i in range(167)]
kokugo_list = []
shakai_list = []
sugaku_list = []
rika_list = []

for i in range(167):
  kokugo_list.append(math.floor(100 * random.random()))

for i in range(167):
  shakai_list.append(math.floor(100 * random.random()))

for i in range(167):
  sugaku_list.append(math.floor(100 * random.random()))

for i in range(167):
  rika_list.append(math.floor(100 * random.random()))

df = pd.DataFrame({'user':user_list, 'kokugo':kokugo_list, 'shakai': shakai_list, 'sugaku': sugaku_list, 'rika': rika_list})
# df.to_csv('user_score.csv')

class_list = []
classes = ['A', 'B', 'C']
for i in range(167):
  value = 3 * random.random()
  integer = math.floor(value)
  class_list.append(classes[integer])
df = pd.DataFrame({'user': user_list, 'class': class_list})
df.to_csv('user_class.csv')
