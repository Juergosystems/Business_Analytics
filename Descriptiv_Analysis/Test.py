import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('train.csv')

df = pd.DataFrame(data)
df1 = df.iloc[:, :72]

print(df1.head())

hist = df1.hist()
plt.show()
