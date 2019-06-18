import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')
df_stores = df_stores.sort_values('Date', ascending=True)

# set color palette to 99 colors
sns.set_palette(sns.color_palette("hls", 45))

# plot line graph showing weekly sales per week grouped by department
df_stores.groupby(['Date', 'Store']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7, figsize=(20,12))

# Shrink current axis by 20%
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0+box.width*0.01, box.y0+box.height*0.05, box.width * 0.9, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12, ncol=3)
ax.set_ylabel('Weekly sales', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
plt.xticks(fontsize=12, rotation = 45)
plt.yticks(fontsize=12)

plt.savefig('../Images/weekly_sales_over_time_stores')