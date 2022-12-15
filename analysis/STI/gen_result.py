import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
import math

df = pd.read_csv('../single_variable_projection.csv')
df.index = df.iloc[...,0].to_numpy()
df = df.drop('Unnamed: 0', axis = 1)

# x2, x7, x6, constant
coff = np.array([0.169, 0.011, 0.051, 5.129])

reg_df = df.iloc[...,[1, 6, 5]][2:]
reg_mat = np.log(reg_df.to_numpy().T)
# print(reg_mat)

res = np.exp(np.dot(coff[:-1], reg_mat) + coff[-1])[8:]
x = np.arange(2000, 2101)

cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']
sns.set(style = 'whitegrid')
plt.plot(x, res, color = cls[3], linewidth = 2)
plt.axhline(y = 450, ls = '--', color = cls[6], label = '450 ppm')

# plt.title('Model 2 Projection')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration / PPM')
print(list(res))

# plt.show()
plt.legend()
plt.savefig('../STI.png', dpi = 300)