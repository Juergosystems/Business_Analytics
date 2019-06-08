import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')
df_stores = df_stores.sort_values('Date', ascending=True)

# create dataframe with data for store 1 only
df_store4 = df_stores[df_stores.Store == 4]
df_store10 = df_stores[df_stores.Store == 10]
df_store14 = df_stores[df_stores.Store == 14]
df_store23 = df_stores[df_stores.Store == 23]
df_store30 = df_stores[df_stores.Store == 30]
df_store43 = df_stores[df_stores.Store == 43]

# set color palette to 99 colors
sns.set_palette(sns.color_palette("hls", 99))

# plot line graph showing weekly sales per week grouped by department
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(20,20))

ax1 = df_store10.groupby(['Date', 'Dept']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7, ax=axes[0], title='Store 10')
ax1.legend('')
ax2 = df_store23.groupby(['Date', 'Dept']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7, ax=axes[1], title='Store 23')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 6, ncol=2)
ax3 = df_store30.groupby(['Date', 'Dept']).sum()['Weekly_Sales'].unstack().plot(linewidth = 0.7, ax=axes[2], title = 'Store 30')
ax3.legend('')

# Put a legend to the right of the current axis
plt.xticks(fontsize=6)

plt.show()