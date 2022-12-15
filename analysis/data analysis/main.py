import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
import math

df1 = pd.read_excel('raw data.xlsx')
df1.index = df1['Year']

sns.set(palette = sns.hls_palette(10, l=0.7, s=0.4))
cls = sns.hls_palette(10, l=0.7, s=0.4)

def data_uniform(x):
	return x / (10 ** 0)

def inverse_data_uniform(x):
	return x * 10 ** 0

# opt example:

def f_1(x, A, B, C, D):
	# return A*np.exp(B * (x - C))+D
	# return A * x ** 2 + B * x + C
	# return A * x + B
	# return A * np.log(B * (x - C)) + D
	return A * np.exp(-(x - B) / C) + D

ind = 'Farmland Area'
start_year = 2000
end_year = 2014

df1 = df1.loc[str(start_year):str(end_year)]
df1.index = range(df1.shape[0])
# print(df1)

x = df1['Year'].to_numpy()
x = x.astype(float)
# df1[ind] = data_uniform(df1[ind])
y1 = data_uniform(df1[ind].to_numpy())
# y2 = df1[ind2].to_numpy()
print(y1)


EPS = 1e-9
bounds_for_ln = ([-np.inf, EPS, EPS, -np.inf], 1e9)
bounds_for_exp = (1. + EPS, np.inf)

x = x - start_year + 1

bd = ([-np.inf, 1, 1, 1], np.inf)
func = optimize.curve_fit(f_1, x, y1, maxfev = 500000, bounds = bd, p0 = [10000, 1000, 1000000, 1000000])[0]
print(f_1(5, *func))
func = tuple(func)
print('qwq', func)

sns.set()

plt.figure(dpi = 150)
# df1[ind2] = data_uniform(df1[ind2])
plt.title('2100 {} Projection'.format(ind))

plot_x = np.linspace(start_year, 2100, 200) - start_year + 1.
# print(inverse_data_uniform(f_1(2100 - start_year + 1, *func)))

correlation = np.corrcoef(x, y1)[0,1]
print('R square = {}'.format(correlation ** 2))

plt.plot(plot_x + start_year - 1, f_1(plot_x, *func), label = 'Predicted {}'.format(ind), color = cls[7])
plt.scatter(x + start_year - 1, y1, label = 'Origin {}'.format(ind), s = 5, color = cls[4], zorder = 5)

plt.xlabel('Year')
plt.ylabel('{} / dollars'.format(ind))
# plt.xticks(np.linspace(1960, 2100, 20))
# plt.yticks(np.linspace(0, 100, 20))
# sns.scatterplot(data = df1, x = 'Year', y = ind2)

plt.subplots_adjust(left = 0.3, right = 0.78)
plt.legend()
plt.show()