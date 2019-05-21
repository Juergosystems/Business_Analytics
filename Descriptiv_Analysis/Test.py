import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('train.csv')

df = pd.DataFrame(data)
df1 = df.iloc[:72:, ]

df1_np = np.array(df1)
print("Shape of the reduced Dataset:", df1_np.shape)

print("\n", df1.head())

hist = df1.hist()
plt.show()
