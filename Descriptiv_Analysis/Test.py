import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('train.csv')

df=pd.DataFrame(data)

plt.plot(x='Store', y='Weekly_Sales')

plt.show()
