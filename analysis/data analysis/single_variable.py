import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
import math

def func1(x, a, b):
	return a * x + b

def func2(x, a, b, c):
	return a * (x ** 2) + b * x + c

def funce(x, a, b, c, d):
	return a * np.exp(b * (x - c)) + d

def funce_dec(x, a, b, c, d):
	return a * np.exp(-(x - b) / c) + d

funcs = {
	'City Population': {
		'func': lambda x: func1(x, *(70094614.92375854, 2122970071.0643442)),
		'start_year': 1990,
		'scale': 10 ** -8
	},
	'GDP': {
		'func': lambda x: func2(x, *(29470450996.762966, -332960767492.89966, 3028809793709.4365)),
		'start_year': 1960,
		'scale': 10 ** -12
	},
	'Industrty Added Value': {
		'func': lambda x: func2(x, *(27411269270.3619, 390171912798.83887, 7428852141065.158)),
		'start_year': 1997,
		'scale': 10 ** -12
	},
	'Agriculture Added Value': {
		'func': lambda x: func2(x, *(5727754187.5758, 82269384635.75714, 938893488494.2206)),
		'start_year': 2000,
		'scale': 10 ** -12
	},
	'Fossil Fuel Percentage': {
		'func': lambda x: func2(x, *(-0.00817825047515327, 0.47602626146526933, 59.74633385243166)),
		'start_year': 1990,
		'scale': 1
	},
	'New Energy Production': {
		'func': lambda x: func2(x, *(4574829335.06564, -58502792003.17906, 301032869031.35126)),
		'start_year': 1992,
		'scale': 10 ** -11
	},
	'Energy per GDP': {
		'func': lambda x: func1(x, *(0.09175169294369538, 5.99539016396565)),
		'start_year': 1991,
		'scale': 1
	},
	'Forest Area': {
		'func': lambda x: funce_dec(x, *(1.6310871633606896, 276.79477631924027, 19.800165408725313, 39480343.086066484)),
		'start_year': 1990,
		'scale': 10 ** -6
	},
	'Farmland Area': {
		'func': lambda x: funce_dec(x, *(0.0006273141678732389, 277.3135754443106, 12.678254533222756, 46958208.02213376)),
		'start_year': 2000,
		'scale': 10 ** -6
	}
}

start, end = 1990, 2100
len = end - start + 1
keys = ['Population']
for i in funcs:
	keys.append(i)
index = np.arange(start, end + 1, 1)

df = pd.DataFrame(data = np.zeros((len, 10)), columns = keys, index = index)

for key in keys:
	if key == 'Population':
		continue
	obj = funcs[key]
	st = obj['start_year']

	len2 = end - st + 1
	x = np.arange(0, len2, 1)
	y = obj['func'](x)
	
	y = y[-len:]
	forw = np.array([np.nan for i in range(len - len2)])
	y = np.hstack((forw, y))
	df[key] = y * obj['scale']

# Deal with Population

def mid_data(l, r):
	x = np.array([0, 4])
	y = np.array([l, r])
	k, b = (r - l) / 4., l
	func = (k, b)

	x_res = np.arange(0, 5)
	return func1(x_res, *func)

df2 = pd.read_excel('raw data.xlsx')
df2.index = df2['Year']
df2 = df2.loc[str(start):'2020']

dat_y = [7.76, 8.14, 8.50, 8.84, 9.16, 9.45, 9.73, 9.97, 10.18, 10.38, 10.55, 10.70, 10.84, 10.95, 11.06, 11.14, 11.21]
pop_y = df2['Population'].to_numpy() / (10 ** 9)

for k in range(16):
	qwq = mid_data(dat_y[k], dat_y[k + 1])
	pop_y = np.hstack((pop_y, qwq))

df['Population'] = pop_y * 10

print(df.head())
df.to_csv('../single_variable_projection.csv')