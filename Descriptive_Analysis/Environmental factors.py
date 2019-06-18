import matplotlib.pyplot as plt
import pandas as pd

# read data
df_features = pd.read_csv('features.csv')
df_features = df_features.sort_values('Date', ascending=True)

# define dataframe that only contains information regarding stores 10, 23 and 30
df_stores = df_features[df_features['Store'].isin([10,23, 30])]

# create plot with four subplots (one line plot for each environmental factors) grouped by the stores
fig, axes = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(10,7))
ax1 = df_stores.groupby(['Date', 'Store']).sum()['Temperature'].unstack().plot(linewidth=0.7, ax=axes[0], title='Temperature', cmap='tab10')
ax1.legend('')
ax1.title.set_size('8')
ax2 = df_stores.groupby(['Date', 'Store']).sum()['Fuel_Price'].unstack().plot(linewidth=0.7, ax=axes[1], title='Fuel price', cmap='tab10')
ax2.legend('')
ax2.title.set_size('8')
ax3 = df_stores.groupby(['Date', 'Store']).sum()['CPI'].unstack().plot(linewidth=0.7, ax=axes[2], title='CPI', cmap='tab10')
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6)
ax3.title.set_size('8')
ax4 = df_stores.groupby(['Date', 'Store']).sum()['Unemployment'].unstack().plot(linewidth=0.7, ax=axes[3], title='Unemployment', cmap='tab10')
ax4.legend('')
ax4.title.set_size('8')

# format axes
plt.xticks(fontsize=6)

# save plot
plt.savefig('../Images/environmental_factors.png')