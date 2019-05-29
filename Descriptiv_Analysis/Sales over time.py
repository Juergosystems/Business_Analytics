import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')
df = df.sort_values('Date', ascending=True)

df_store1 = df[df.Store == 1]

# plot graph with grouping
df_store1.groupby(['Date', 'Dept']).sum()['Weekly_Sales'].unstack().plot(kind='scatter')

ax = plt.subplot(111)

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6, ncol=3)
plt.xticks(fontsize=6, rotation = 45)
plt.title('Weekly Sales per Department, Store 1')
plt.show()