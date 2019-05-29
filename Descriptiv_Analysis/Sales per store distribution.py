import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')

fig, ax = plt.subplots()

scatter = ax.scatter(x=df.Store, y=df.Weekly_Sales, c=df.IsHoliday, alpha=0.8, s=10, edgecolors='none', cmap='winter')

#produce legend with unique colors from scatter
legend1 = ax.legend(*scatter.legend_elements(), loc="upper right", title="Holiday")
ax.add_artist(legend1)
plt.title('Distribution of Weekly Sales per Store')

plt.show()
