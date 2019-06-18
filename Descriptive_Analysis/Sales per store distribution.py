import matplotlib.pyplot as plt
import pandas as pd

# read data set
df = pd.read_csv('train.csv')

fig, ax = plt.subplots()

# plot scatter graph of weekly sales per store with the colour of the points indicating holiday weekw
scatter = ax.scatter(x=df.Store, y=df.Weekly_Sales, c=df.IsHoliday, alpha=0.8, s=10, edgecolors='none', cmap='winter')

plt.legend()
# legend with unique colors from scatter
legend1 = ax.legend(*scatter.legend_elements(), title="Holiday")
ax.add_artist(legend1)

plt.savefig('../Images/scatter_plot_holidays')