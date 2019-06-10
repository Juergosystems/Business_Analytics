import matplotlib
matplotlib.use('MacOSX')
import pandas as pd
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import matplotlib.pyplot as plt

# read data
train = pd.read_csv("../Data/train.csv",sep=',', header=0)
features = pd.read_csv("../Data/features.csv",sep=',', header=0).drop(columns=['IsHoliday'])
stores = pd.read_csv("../Data/stores.csv",sep=',', header=0)

# merge the different files into one dataset to work with
dataset = train.merge(stores, how='left').merge(features, how='left')
dataset = dataset[['Weekly_Sales','Store', 'Dept', 'Date', 'IsHoliday', 'Type', 'Size', 'Temperature', 'Fuel_Price',
                   'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI', 'Unemployment']]

def plot_corr(df):
    plt.figure(figsize=(10,10))
    plt.imshow(df.corr(), cmap=plt.cm.Reds, interpolation='nearest')
    plt.colorbar()
    tick_marks = [i for i in range(len(df.columns))]
    plt.xticks(tick_marks, df.columns, rotation='vertical')
    plt.yticks(tick_marks, df.columns)
    plt.title('Correlation Matrix')
    plt.show()

dataset_for_corr = dataset.drop(columns=['Type', 'Date'])

plot_corr(dataset_for_corr)
