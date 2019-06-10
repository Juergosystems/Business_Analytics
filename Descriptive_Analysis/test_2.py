import matplotlib.pyplot as plt
import pandas as pd

df_features = pd.read_csv('features.csv')
df_features = df_features.sort_values('Date', ascending=True)

df_features.plot(kind='box')

plt.show()