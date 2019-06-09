import matplotlib.pyplot as plt
import pandas as pd

df_features = pd.read_csv('features.csv')
df_features = df_features.sort_values('Date', ascending=True)

df_store10 = df_features[df_features['Store'].isin([10,23, 30])]

fig, axes = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(10,7))
ax1 = df_store10.groupby(['Date', 'Store']).sum()['Temperature'].unstack().plot(linewidth=0.7, ax=axes[0], title='Temperature', cmap='tab10')
ax1.legend('')
ax1.title.set_size('8')
ax2 = df_store10.groupby(['Date', 'Store']).sum()['Fuel_Price'].unstack().plot(linewidth=0.7, ax=axes[1], title='Fuel price', cmap='tab10')
ax2.legend('')
ax2.title.set_size('8')
ax3 = df_store10.groupby(['Date', 'Store']).sum()['CPI'].unstack().plot(linewidth=0.7, ax=axes[2], title='CPI', cmap='tab10')
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6)
ax3.title.set_size('8')
ax4 = df_store10.groupby(['Date', 'Store']).sum()['Unemployment'].unstack().plot(linewidth=0.7, ax=axes[3], title='Unemployment', cmap='tab10')
ax4.legend('')
ax4.title.set_size('8')

plt.xticks(fontsize=6)

plt.show()