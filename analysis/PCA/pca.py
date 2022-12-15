import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
import math

pca_mat = pd.read_csv('pca_mat.csv').to_numpy()
linear_reg_mat = np.array([2.8360146591749693, 2.2049217781590826, 0.5752225714465027, 201.81672619659412])

def calc(x):
	return np.dot(linear_reg_mat[:-1], np.dot(pca_mat, x)) + linear_reg_mat[-1]

df = pd.read_csv('../single_variable_projection.csv')
df.index = df.iloc[...,0].to_numpy()
df = df.drop('Unnamed: 0', axis = 1)

# x_test = df.loc[2020].to_numpy()
# print(x_test)
# print(calc(x_test))

start, end = 2000, 2130

x = df.loc[start:end].to_numpy().T
y = calc(x)
x_plot = np.arange(start, end + 1)
print(y)

sns.set(style = 'whitegrid')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']
plt.plot(x_plot, y, color = cls[3], linewidth = 2)
plt.axhline(y = 450, ls = '--', color = cls[6], label = '450 ppm')

# print(y)
# plt.title('Model 1 Projection')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration / PPM')

print(np.dot(linear_reg_mat[:-1], pca_mat))

print(list(x_plot), list(y))
plt.legend()
plt.show()
# plt.savefig('../PCA.png', dpi=300)