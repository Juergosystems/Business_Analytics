import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')

# create boxplot for weeks without holidays
ax = df_stores.boxplot(by='Store', column='Weekly_Sales', figsize=(20,10), showfliers=False)
ax.set_ylabel("Weekly Sales")
plt.title("")
plt.suptitle("")

plt.show()