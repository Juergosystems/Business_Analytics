import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_stores = pd.read_csv('train.csv')

df_stores.boxplot(by='Store', column='Weekly_Sales', figsize=(20,10))

#ax.set_ylabel("Weekly Sales")
plt.title("")
plt.suptitle("")

plt.show()