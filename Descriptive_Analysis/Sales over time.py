import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')
df_stores = df_stores.sort_values('Date', ascending=True)

# create dataframe with data for store 1 only
df_store1 = df_stores[df_stores.Store == 1]

# set color palette to 99 colors
sns.set_palette(sns.color_palette("hls", 99))

# plot line graph showing weekly sales per week grouped by department
df_store1.groupby(['Date', 'Dept']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7)

# Shrink current axis by 20%
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6, ncol=3)
plt.xticks(fontsize=6, rotation = 45)

plt.show()