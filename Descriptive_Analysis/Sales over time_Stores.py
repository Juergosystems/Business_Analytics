import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates

# read data set
df_stores = pd.read_csv('train.csv')

# sort data by date
df_stores = df_stores.sort_values('Date', ascending=True)

# set color palette to 45 colors
sns.set_palette(sns.color_palette("hls", 45))

# plot line graph with weekly sales over time grouped by store
df_stores.groupby(['Date', 'Store']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7, figsize=(10,10))

# Shrink current axis by 20%
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6, ncol=3)

# format axes
plt.xticks(fontsize=6, rotation = 45)
ax.set_ylabel('Weekly Sales')
plt.yticks(fontsize=6)


plt.show()