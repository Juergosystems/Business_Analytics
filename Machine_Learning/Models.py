import numpy as np
import matplotlib
matplotlib.use('MacOSX')
import pandas as pd
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn.decomposition import KernelPCA
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

# Data Import
########################################################################################################################

# read data
train = pd.read_csv("../Data/train.csv",sep=',', header=0)
features = pd.read_csv("../Data/features.csv",sep=',', header=0).drop(columns=['IsHoliday'])
stores = pd.read_csv("../Data/stores.csv",sep=',', header=0)

# merge the different files into one dataset to work with
dataset = train.merge(stores, how='left').merge(features, how='left')
dataset = dataset[['Weekly_Sales','Store', 'Dept', 'Date', 'IsHoliday', 'Type', 'Size', 'Temperature', 'Fuel_Price',
                   'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI', 'Unemployment']]

# Preprocessing
########################################################################################################################
pd.set_option('display.max_columns', 17)
pd.set_option('display.width', 300)

# Overview before preprocessing
summary = dataset.describe()
summary.to_excel('../Data/summary_before_preprocessing.xlsx', header=True, encoding='utf8')

# encode strings to integer
cat_col = ['IsHoliday','Type']
for col in cat_col:
    encoder = preprocessing.LabelEncoder()
    encoder.fit(dataset[col].values.astype('str'))
    dataset[col] = encoder.transform(dataset[col].values.astype('str'))

# Replace Nan with 0
dataset[['MarkDown1','MarkDown2','MarkDown3','MarkDown4', 'MarkDown5']] = dataset[['MarkDown1','MarkDown2','MarkDown3',
                                                                                   'MarkDown4','MarkDown5']].fillna(0)

# Encode Weekdate to number of month to use it as a feature
dataset['Month'] = pd.to_datetime(dataset['Date']).dt.month
dataset = dataset.drop(columns=["Date"])

# Remove rows, which contain bad quality data, e.q. negative values in specific columns
for i in ['Weekly_Sales','MarkDown2','MarkDown3']:
    indexNames = dataset[dataset[i] < 0 ].index
    dataset.drop(indexNames , inplace=True, axis=0)

# Overview after quality preprocessing
summary = dataset.describe()
summary.to_excel('../Data/summary_after_quality_preprocessing.xlsx', header=True, encoding='utf8')

# Standardize the features
X_dataset = dataset.drop(columns=['Weekly_Sales'])
column_names = list(X_dataset.columns.values)
scaler = StandardScaler()
#scaler = MinMaxScaler()
#scaler = RobustScaler()
X_dataset_scaled = scaler.fit_transform(X_dataset)

# Overview after scaling preprocessing
X_train = pd.DataFrame(X_dataset_scaled, columns=column_names)
dataset = pd.concat([dataset['Weekly_Sales'], X_train], axis=1)
summary = dataset.describe()
summary.to_excel('../Data/summary_after_scaling_preprocessing.xlsx', header=True, encoding='utf8')

# Modeling
########################################################################################################################

