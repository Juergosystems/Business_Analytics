import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import seaborn as sns

# read data set
df_train = pd.read_csv('train.csv')

# sort data by date
df_train = df_train.sort_values('Date', ascending=True)

# set color palette to 45 colors
sns.set_palette(sns.color_palette("hls", 45))

# plot graph with grouping
df_train.groupby(['Date', 'Store']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7)

ax = plt.subplot(111)

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6, ncol=3)
plt.xticks(fontsize=6, rotation = 45)

plt.show()