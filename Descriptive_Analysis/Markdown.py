import matplotlib.pyplot as plt
import pandas as pd

# read data
df_features = pd.read_csv("../Data/features.csv",sep=',', header=0)
df_features = df_features.sort_values('Date', ascending=True)

# create dataframe for store 10, 23 and 30 only
df_stores = df_features[df_features['Store'].isin([10,23, 30])]

# create plot with 5 subplots, one for each markdown
fig, axes = plt.subplots(nrows=5, ncols=1, sharex=True, figsize=(10,7))
ax1 = df_stores.groupby(['Date', 'Store']).sum()['MarkDown1'].unstack().plot(linewidth=0.7, ax=axes[0], title='Markdown 1', cmap='tab10')
ax1.legend('')
ax1.title.set_size('8')
ax2 = df_stores.groupby(['Date', 'Store']).sum()['MarkDown2'].unstack().plot(linewidth=0.7, ax=axes[1], title='Markdown 2', cmap='tab10')
ax2.legend('')
ax2.title.set_size('8')
ax3 = df_stores.groupby(['Date', 'Store']).sum()['MarkDown3'].unstack().plot(linewidth=0.7, ax=axes[2], title='Markdown 3', cmap='tab10')
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6)
ax3.title.set_size('8')
ax4 = df_stores.groupby(['Date', 'Store']).sum()['MarkDown4'].unstack().plot(linewidth=0.7, ax=axes[3], title='Markdown 4', cmap='tab10')
ax4.legend('')
ax4.title.set_size('8')
ax5 = df_stores.groupby(['Date', 'Store']).sum()['MarkDown5'].unstack().plot(linewidth=0.7, ax=axes[4], title='Markdown 5', cmap='tab10')
ax5.legend('')
ax5.title.set_size('8')

# format axes
plt.xticks(fontsize=6)

plt.savefig('../Images/markdowns.png')
