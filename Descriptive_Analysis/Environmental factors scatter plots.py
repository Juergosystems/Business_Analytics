import matplotlib.pyplot as plt
import pandas as pd

# read data
df_features = pd.read_csv('features.csv')
df_features = df_features.sort_values('Date', ascending=True)

# create dataframes for the stores only
df_stores = df_features[df_features['Store'].isin([10,23, 30])]
df_store10 = df_features[df_features.Store == 10]
df_store23 = df_features[df_features.Store == 23]
df_store30 = df_features[df_features.Store == 30]

# create plot with 15 subplots, one for each store per markdown
fig, axes = plt.subplots(nrows=3, ncols=5, sharex=True, figsize=(12,10))
ax1 = df_store10.boxplot(by='IsHoliday', column='MarkDown1', ax=axes[0,0])
axes[0,0].set_title('Markdown 1', fontsize=10)
ax1.set_ylabel("Store 10")
ax2 = df_store23.boxplot(by='IsHoliday', column='MarkDown1', ax=axes[1,0])
axes[1,0].set_title('')
ax2.set_ylabel("Store 23")
ax3 = df_store30.boxplot(by='IsHoliday', column='MarkDown1', ax=axes[2,0])
axes[2,0].set_title('')
ax3.set_ylabel("Store 30")

ax4 = df_store10.boxplot(by='IsHoliday', column='MarkDown2', ax=axes[0,1])
axes[0,1].set_title('Markdown 2', fontsize=10)
ax5 = df_store23.boxplot(by='IsHoliday', column='MarkDown2', ax=axes[1,1])
axes[1,1].set_title('')
ax6 = df_store30.boxplot(by='IsHoliday', column='MarkDown2', ax=axes[2,1])
axes[2,1].set_title('')

ax7 = df_store10.boxplot(by='IsHoliday', column='MarkDown3', ax=axes[0,2])
axes[0,2].set_title('Markdown 3', fontsize=10)
ax8 = df_store23.boxplot(by='IsHoliday', column='MarkDown3', ax=axes[1,2])
axes[1,2].set_title('')
ax9 = df_store30.boxplot(by='IsHoliday', column='MarkDown3', ax=axes[2,2])
axes[2,2].set_title('')

ax10 = df_store10.boxplot(by='IsHoliday', column='MarkDown4', ax=axes[0,3])
axes[0,3].set_title('Markdown 4', fontsize=10)
ax11 = df_store23.boxplot(by='IsHoliday', column='MarkDown4', ax=axes[1,3])
axes[1,3].set_title('')
ax12 = df_store30.boxplot(by='IsHoliday', column='MarkDown4', ax=axes[2,3])
axes[2,3].set_title('')

ax13 = df_store10.boxplot(by='IsHoliday', column='MarkDown5', ax=axes[0,4])
axes[0,4].set_title('Markdown 5', fontsize=10)
ax14 = df_store23.boxplot(by='IsHoliday', column='MarkDown5', ax=axes[1,4])
axes[1,4].set_title('')
ax15 = df_store30.boxplot(by='IsHoliday', column='MarkDown5', ax=axes[2,4])
axes[2,4].set_title('')

ax1.set_xlabel('')
ax2.set_xlabel('')
ax3.set_xlabel('')
ax4.set_xlabel('')
ax5.set_xlabel('')
ax6.set_xlabel('')
ax7.set_xlabel('')
ax8.set_xlabel('')
ax8.set_xlabel('')
ax10.set_xlabel('')
ax11.set_xlabel('')
ax12.set_xlabel('')
ax13.set_xlabel('')
ax14.set_xlabel('')
ax15.set_xlabel('')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.08, right=0.98, hspace=0.25,
                    wspace=0.35)

plt.suptitle('')

plt.savefig('../Images/environmental_factors_boxplots')