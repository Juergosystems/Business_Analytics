# -*- coding: utf-8 -*-
"""Models_with_markdown.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ORw6UQQiAgnyk3sOHyCFfl_KDqyA8RkX

# Business Analytics Models
"""

"""## Import Packages & Set global variables"""

import warnings
import numpy as np
import pandas as pd
import datetime as dt
from keras import optimizers
from keras.utils import plot_model
from keras.models import Sequential, Model
from sklearn import preprocessing
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error

# %matplotlib inline
pd.set_option('display.float_format', lambda x: '%.4f' % x)
warnings.filterwarnings("ignore")

# Setting seeds to make the project more reproducible.
from numpy.random import seed
seed(0)
from tensorflow import set_random_seed
set_random_seed(0)

from sklearn.ensemble import RandomForestRegressor
import seaborn as sns; sns.set(style="ticks", color_codes=True)

"""## Data import"""

# read data
train = pd.read_csv("../Data/train.csv",sep=',', header=0)
features = pd.read_csv("../Data/features.csv",sep=',', header=0).drop(columns=['IsHoliday'])
stores = pd.read_csv("../Data/stores.csv",sep=',', header=0)

# merge the different files into one dataset to work with
dataset = train.merge(stores, how='left').merge(features, how='left')
dataset = dataset[['Weekly_Sales','Store', 'Dept', 'Date', 'IsHoliday', 'Type', 'Size', 'Temperature', 'Fuel_Price',
                   'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI', 'Unemployment']]

"""## Preprocessing

### General preprocessing

Overview before preprocessing
"""

pd.set_option('display.max_columns', 17)
pd.set_option('display.width', 300)

print(dataset.head())
print('\n',dataset.describe())

"""encode strings to integer"""

cat_col = ['IsHoliday','Type']

for col in cat_col:
    encoder = preprocessing.LabelEncoder()
    encoder.fit(dataset[col].values.astype('str'))
    dataset[col] = encoder.transform(dataset[col].values.astype('str'))
    
dataset.head()

"""Replace Nan with 0 in the MarkDown features"""

dataset[['MarkDown1','MarkDown2','MarkDown3','MarkDown4', 'MarkDown5']] = dataset[['MarkDown1','MarkDown2','MarkDown3',
                                                                                   'MarkDown4','MarkDown5']].fillna(0)
dataset.head()

"""Remove rows, which contain bad quality data, e.q. negative values in specific columns"""

for i in ['Weekly_Sales','MarkDown2','MarkDown3']:
    indexNames = dataset[dataset[i] < 0 ].index
    dataset.drop(indexNames , inplace=True, axis=0)

"""### Time period preprocessing of the dataset"""

dataset['Date'] = pd.to_datetime(dataset['Date'], format='%Y/%m/%d')
dataset['Date'] = dataset['Date'].dt.date
first_date = (np.min(dataset['Date']))
last_date = (np.max(dataset['Date']))
print('first date:',first_date,'\nlast date:',last_date)

"""Only consider the last year to predict the next week. (54 weeks in total) Since there is a lot of missing data in the beginning of the recording."""

one_year = last_date - pd.Timedelta(54, 'w')
dataset = dataset.loc[dataset['Date'] > one_year]

"""Creating Time-series of sales by Store and Department using Pivot"""

dataset_sales_series = dataset.pivot_table(index =['Store', 'Dept'], columns='Date', values='Weekly_Sales', fill_value=0).reset_index()

"""Count the numbers of zero/missing values per row."""

dataset_sales_series['Number of missing values'] = (dataset_sales_series == 0).astype(int).sum(axis=1)

"""Delete all the rows, which have more then 10 % of missing values. (>5)"""

dataset_sales_series = dataset_sales_series.loc[dataset_sales_series['Number of missing values'] <= 5]
dataset_sales_series = dataset_sales_series.drop(columns='Number of missing values')
dataset_sales_series.head()

"""Adding the other features to get a complete dataset to work with."""

dataset_series_total = dataset_sales_series.merge(stores, how='left')

cat_col = ['Type']
for col in cat_col:
    encoder = preprocessing.LabelEncoder()
    encoder.fit(dataset_series_total[col].values.astype('str'))
    dataset_series_total[col] = encoder.transform(dataset_series_total[col].values.astype('str'))
    
dataset_series_total.head()

"""### Creating Trainings- and Validation-Set"""

X_df = dataset_series_total.drop(columns=['Store', dt.date(2012,10,26)])
Y_df = dataset_series_total[[dt.date(2012,10,26)]]

train_df, valid_df, Y_train_df, Y_valid_df = train_test_split(X_df,Y_df, test_size=0.1, random_state=0)

X_train_df = train_df.drop(columns=['Dept','Type','Size'])
X_valid_df = valid_df.drop(columns=['Dept','Type','Size'])

print('X_train_df:','\n','\n', X_train_df.head(),)

"""##  LSTM

### Preprocessing

#### Scaling
"""

scaler = MinMaxScaler()
X_train_np = scaler.fit_transform(np.array(X_train_df))
X_valid_np = scaler.transform(np.array(X_valid_df))

"""#### Shaping"""

X_train_lstm = X_train_np.reshape((X_train_np.shape[0], X_train_np.shape[1],1))
X_valid_lstm = X_valid_np.reshape((X_valid_np.shape[0], X_valid_np.shape[1],1))

print(X_train_lstm.shape)
print(X_valid_lstm.shape)

"""### Autoencoder Model"""

serie_size =  X_train_lstm.shape[1]
n_features =  X_train_lstm.shape[2] 

epochs = 5
batch = 128
lr = 0.0001

encoder_decoder = Sequential()
encoder_decoder.add(LSTM(serie_size, activation='relu', input_shape=(serie_size, n_features), return_sequences=True))
encoder_decoder.add(LSTM(10, activation='relu', return_sequences=True))
encoder_decoder.add(LSTM(1, activation='relu'))
encoder_decoder.add(RepeatVector(serie_size))
encoder_decoder.add(LSTM(serie_size, activation='relu', return_sequences=True))
encoder_decoder.add(LSTM(10, activation='relu', return_sequences=True))
encoder_decoder.add(TimeDistributed(Dense(1)))
encoder_decoder.summary()

adam = optimizers.Adam(lr)
encoder_decoder.compile(loss='mse', optimizer=adam)

encoder_decoder_history = encoder_decoder.fit(X_train_lstm, X_train_lstm, epochs=epochs, batch_size=batch, verbose=2)

"""### Encoder Model

Only taking the encoding part of the Autoencoder
"""

encoder = Model(inputs=encoder_decoder.inputs, outputs=encoder_decoder.layers[2].output)
plot_model(encoder_decoder, show_shapes=True, to_file='../Images/encoder_decoder_reconstruct_lstm.png')
plot_model(encoder, show_shapes=True, to_file='../Images/encoder_lstm.png')

"""Encode the time-series of the train set"""

X_train_encoded = encoder.predict(X_train_lstm)
X_valid_encoded = encoder.predict(X_valid_lstm)
print('Encoded time-series shape', X_train_encoded.shape)

# print('Encoded time-series sample:')
# for i in range(10): 
#   print(X_train_encoded[i])

"""Create new Dataset for basic Regressor by stacking the encoded feature together with the current sales, the department number, the store size and the store type."""

train_df['Encoded'] = X_train_encoded
train_df['Label'] = Y_train_df

valid_df['Encoded'] = X_valid_encoded
valid_df['Label'] = Y_valid_df

X_train_basic = train_df[[dt.date(2012,10,19), 'Encoded','Dept', 'Type', 'Size']]
X_valid_basic = valid_df[[dt.date(2012,10,19), 'Encoded','Dept', 'Type', 'Size']]

Y_train_basic = train_df['Label']
Y_valid_basic = valid_df['Label']

X_train_basic.describe()

"""## Random Forest Regressor

### Preprocessing

"""#### Create Numpy-Array"""

X_train_basic_np = scaler.fit_transform(np.array(X_train_basic))
X_valid_basic_np = scaler.transform(np.array(X_valid_basic))

Y_train_basic_np = np.array(Y_train_basic)
Y_valid_basic_np = np.array(Y_valid_basic)

"""### Set up"""

RFR_basic = RandomForestRegressor(n_estimators=100,max_features=2, verbose=0, n_jobs=-1)

"""### Train"""

RFR_basic.fit(X_train_basic_np, Y_train_basic_np)

"""### Validation"""

Y_predict = RFR_basic.predict(X_valid_basic_np)
print("Mean absolute Error of basic model:", np.round(mean_absolute_error(Y_valid_basic_np,Y_predict),2),'\n')

feat_importance = pd.DataFrame(RFR_basic.feature_importances_.reshape(1,5), columns=['Current Sales','Past Sales','Dept', 'Type', 'Size'])

# print('Feature Importance:','\n','\n',feat_importance)

"""## Baseline Model

For this regressor, we only use the current sales to predict the sales of the next week.

### Preprocessing
"""

X_train_baseline = train_df[[dt.date(2012,10,19)]]
Y_train_baseline = train_df['Label']

X_valid_baseline = valid_df[[dt.date(2012,10,19)]]
Y_valid_baseline = valid_df['Label']

X_train_baseline_np = scaler.fit_transform(np.array(X_train_baseline))
X_valid_baseline_np = scaler.transform(np.array(X_valid_baseline))

Y_train_baseline_np = np.array(Y_train_baseline)
Y_valid_baseline_np = np.array(Y_valid_baseline)

"""### Modeling"""

RFR_basic = RandomForestRegressor(n_estimators=100,max_features=1, verbose=0, n_jobs=-1)

RFR_basic.fit(X_train_baseline_np, Y_train_baseline_np)

Y_predict = RFR_basic.predict(X_valid_baseline_np)

print("Mean absolute Error of baseline model:", np.round(mean_absolute_error(Y_valid_baseline_np,Y_predict),2),'\n')
