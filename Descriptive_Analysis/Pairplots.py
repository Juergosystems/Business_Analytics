import matplotlib
matplotlib.use('MacOSX')
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

dataset1 = dataset.drop(columns=[ 'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5','Date','Store','CPI','Unemployment' ,'IsHoliday','Temperature', 'Fuel_Price'])

sns.pairplot(dataset1)
plt.show()
