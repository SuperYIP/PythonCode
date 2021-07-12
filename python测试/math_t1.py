import pandas as pd
import numpy as np


inp = [{'c1':1, 'c2':1}, {'c1':2, 'c2':2},{'c1':1, 'c2':2}, {'c1':2, 'c2':3}, {'c1':2, 'c2':4}, {'c1':2, 'c2':5}]
df = pd.DataFrame(inp)

print(df)
print('--------')
df = df.sort_values(by=['c1']).sum()
print(df)