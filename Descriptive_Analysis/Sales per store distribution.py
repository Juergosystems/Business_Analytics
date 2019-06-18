import matplotlib.pyplot as plt
import pandas as pd

# read data set
df_train = pd.read_csv("../Data/train.csv",sep=',', header=0)

fig, ax = plt.subplots()

# plot scatter graph of weekly sales per store with the colour of the points indicating holiday weekw
scatter = ax.scatter(x=df_train.Store, y=df_train.Weekly_Sales, c=df_train.IsHoliday, alpha=0.8, s=10, edgecolors='none', cmap='winter')

plt.legend()
# legend with unique colors from scatter
legend1 = ax.legend(*scatter.legend_elements(), title="Holiday")
ax.add_artist(legend1)

plt.savefig('../Images/scatter_plot_holidays.png')
