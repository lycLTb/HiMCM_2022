import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize, integrate
import math

def read_pre():
	df = pd.read_csv('../single_variable_projection.csv')
	df.index = df.iloc[...,0].to_numpy()
	return df.drop('Unnamed: 0', axis = 1)

df = read_pre()
NEpercentage = (100. - df['Fossil Fuel Percentage'].to_numpy()) / 100.
coff = np.array([15, 5])
cP = df['City Population'].to_numpy()
cP = np.array([cP, df['Population'].to_numpy() - cP])

population_scale = 10 ** 8
ppm2mass = 7.828 * 10 ** 9

CEindex = np.dot(coff, cP) * population_scale / ppm2mass

scale = np.array([-5, 0.3])
err = 1.
indexs = np.dot(scale, np.vstack((NEpercentage, CEindex))) + err

sns.set(style = 'whitegrid')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']
xx = np.arange(1990, 2101)

parameters = np.polyfit(xx, indexs, 3)
func_3 = np.poly1d(parameters)


def f0(y, t):
	if y <= 450:
		return -0.00002 * y ** 1.5
	else:
		return -np.exp((y - 450) / 10)

def f1(x):
	return func_3(x)

def func(t, y):
	return f0(y, t) + f1(t)

start, end = 2020, 2100

result = integrate.solve_ivp(func, (start, end), [414.24], dense_output = True)
x = np.arange(start - 20, end + 1)
y = result.sol(x)[0]

plt.plot(x, y, color = cls[3], linewidth = 2)
plt.axhline(y = 450, ls = '--', color = cls[6], label = '450 ppm')
print(result.sol(2050))
plt.xlabel('Year')
plt.ylabel('CO2 Concentration / PPM')
# plt.title('Model 3 Projection')

# print(list(y))
plt.legend()
# plt.show()
plt.savefig('../ODE.png', dpi=300)