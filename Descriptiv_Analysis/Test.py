import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


### Read in the Datafiles
#############################################################################################
data = pd.read_csv('train.csv')
df = pd.DataFrame(data)
print(df.head(), "\n")

### Only take the first 100 rows of the Datafile
#############################################################################################
df_reduced= df.iloc[:100:, ]

### Change the pandas Dataframe to a NumpyAarray to check the shape of the reduced Dataset
#############################################################################################
df1_np = np.array(df_reduced)
print("Shape of the reduced Dataset:", df1_np.shape, " (row,column)")

### Plot a Histogramm of the reduced Dataset
#############################################################################################
#hist = df_reduced.hist()
#plt.show()

hist = df
plt.show()
