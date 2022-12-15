import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
import math

x = np.arange(2020, 2101, 5)
y = [7.76, 8.14, 8.50, 8.84, 9.16, 9.45, 9.73, 9.97, 10.18, 10.38, 10.55, 10.70, 10.84, 10.95, 11.06, 11.14, 11.21]
cls = sns.hls_palette(10, l=0.7, s=0.4)
plt.figure(dpi = 150)

df1 = pd.read_excel('raw data.xlsx')
df1.index = df1['Year']
df1 = df1.loc['1960':'2020']

x = np.hstack((np.arange(1960, 2021, 1), x))
y = np.hstack((df1['Population'].to_numpy() / (10 ** 9), y))
print(x)

sns.set()
plt.plot(x, y, label = 'Predicted Population', color = cls[7])

plt.title('2100 Population Projection')
plt.xlabel('Year')
plt.ylabel('Population / billion')
plt.legend()
plt.show()