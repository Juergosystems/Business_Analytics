import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('train.csv')

df = pd.DataFrame(data)
df = df['Date']
df.hist(bins=5)

