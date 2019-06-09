import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')

# create dataset only containing weeks without holidays
df_Holiday = df_stores[df_stores.IsHoliday == 1]

# create boxplot for weeks without holidays
ax = df_Holiday.boxplot(by='Store', column='Weekly_Sales', figsize=(20,10))
ax.set_ylabel("Weekly Sales")
plt.title("")
plt.suptitle("")

plt.show()