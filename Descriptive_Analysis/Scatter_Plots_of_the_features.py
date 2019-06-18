import matplotlib
matplotlib.use('tkagg')
import pandas as pd
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import matplotlib.pyplot as plt
from sklearn import preprocessing

# read data
train = pd.read_csv("../Data/train.csv",sep=',', header=0)
features = pd.read_csv("../Data/features.csv",sep=',', header=0).drop(columns=['IsHoliday'])
stores = pd.read_csv("../Data/stores.csv",sep=',', header=0)

# merge the different files into one dataset to work with
dataset = train.merge(stores, how='left').merge(features, how='left')
dataset = dataset[['Weekly_Sales','Store', 'Dept','CPI', 'Unemployment' , 'IsHoliday', 'Type', 'Size', 'Temperature', 'Fuel_Price',
                   'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5','Date']]

cat_col = ['IsHoliday','Type']

for col in cat_col:
    encoder = preprocessing.LabelEncoder()
    encoder.fit(dataset[col].values.astype('str'))
    dataset[col] = encoder.transform(dataset[col].values.astype('str'))

# Plot all the features agains the Weekly_Sales
rows = [3,2]
r = 0
for i in [1,10]:
    fig, ax = plt.subplots(ncols=3,nrows=rows[r],figsize=(9,rows[r]*3))
    plt.subplots_adjust(wspace=.7, hspace=.5)
    for row in ax:
        for col in row:
                col.scatter(dataset[list(dataset.columns.values)[i]], dataset['Weekly_Sales'], s=[5])
                col.set_ylabel('Weekly_Sales')
                col.set_xlabel(list(dataset.columns.values)[i])
                if i == 15:
                    col.set_visible(False)
                i += 1
    plt.savefig('../Images/Scatterplots' + str(r) + '.png')

    r += 1

