import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


### Read in the Datafiles
#############################################################################################
data = pd.read_csv('train.csv')
df = pd.DataFrame(data)

### Only take the first 100 rows of the Datafile
#############################################################################################
df1 = df.iloc[:100:, ]
print(df1.head(), "\n")

### Change the pandas Dataframe to a NumpyAarray to check the shape of the reduced Dataset
#############################################################################################
df1_np = np.array(df1)
print("Shape of the reduced Dataset:", df1_np.shape)

### Plot a Histogramm of the reduced Dataset
#############################################################################################
hist = df1.hist()
plt.show()
