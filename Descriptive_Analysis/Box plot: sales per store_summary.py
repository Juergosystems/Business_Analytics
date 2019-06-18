import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv("../Data/train.csv",sep=',', header=0)

# create dataset only containing weeks without holidays
df_noHoliday = df_stores[df_stores.IsHoliday == 0]
df_Holiday = df_stores[df_stores.IsHoliday == 1]

plt.rc('xtick',labelsize=8)
plt.rc('ytick',labelsize=8)

# create boxplot with subplots for all weeks, weeks without holidays and weeks with holidays
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(20,20))
ax1 = df_stores.boxplot(by='Store', column='Weekly_Sales', ax=axes[0])
axes[0].set_title('Weekly sales all weeks', fontsize=10)
ax2 = df_noHoliday.boxplot(by='Store', column='Weekly_Sales', ax=axes[1])
axes[1].set_title('Weekly sales - no holidays', fontsize=10)
ax3 = df_Holiday.boxplot(by='Store', column='Weekly_Sales', ax=axes[2])
axes[2].set_title('Weekly sales - holidays', fontsize=10)
ax1.set_xlabel('')
ax2.set_xlabel('')
ax2.set_ylabel("Weekly Sales")
plt.suptitle('')

plt.savefig('../Images/boxplots_weekly_sales.png')
