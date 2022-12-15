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
	'Population': {
		'start_year': 1960,
		'end_year': 2020,
		'scale': 10 ** -8
	},
	'City Population': {
		'start_year': 1990,
		'end_year': 2020,
		'scale': 10 ** -8,
		'type': 'func1'
	},
	'GDP': {
		'start_year': 1990,
		'end_year': 2020,
		'scale': 10 ** -12,
		'type': 'func2'
	},
	'Industrty Added Value': {
		'start_year': 1997,
		'end_year': 2014,
		'scale': 10 ** -12,
		'type': 'func2'
	},
	'Agriculture Added Value': {
		'start_year': 2000,
		'end_year': 2014,
		'scale': 10 ** -12,
		'type': 'func2'
	},
	'Fossil Fuel Percentage': {
		'start_year': 1990,
		'end_year': 2015,
		'scale': 1,
		'type': 'func2'
	},
	'New Energy Production': {
		'start_year': 1992,
		'end_year': 2015,
		'scale': 10 ** -11,
		'type': 'func2'
	},
	'Energy per GDP': {
		'start_year': 1991,
		'end_year': 2014,
		'scale': 1,
		'type': 'func1'
	},
	'Forest Area': {
		'start_year': 1990,
		'end_year': 2016,
		'scale': 10 ** -6,
		'type': 'funce_dec'
	},
	'Farmland Area': {
		'start_year': 2000,
		'end_year': 2020,
		'scale': 10 ** -6,
		'type': 'funce_dec'
	}
}

str2func = {
	'func1': func1,
	'func2': func2,
	'funce_dec': funce_dec
}

start, end = 1990, 2100
len = end - start + 1
keys = []
for i in funcs:
	keys.append(i)
index = np.arange(start, end + 1, 1)

df = pd.DataFrame(data = np.zeros((len, 10)), columns = keys, index = index)
df_origin = pd.read_excel('raw data backup.xlsx')
df_origin.index = df_origin['Year']

def fitCurve(key):
	obj = funcs[key]
	typ = obj['type']
	p0type = {
		'func1': [10000, 10000],
		'func2': [10000, 10000, 10000],
		'funce_dec': [10000, 1000, 1000000, 1000000]
	}

	l, r = obj['start_year'], obj['end_year']
	len = r - l + 1

	x = np.arange(0, len)

	bdtype = {
		'func1': (-np.inf, np.inf),
		'func2': (-np.inf, np.inf),
		'funce_dec': ([-np.inf, 1, 1, 1], np.inf)
	}


	y1 = df_origin[key].loc[str(l):str(r)].to_numpy()
	print(y1)
	paras = optimize.curve_fit(str2func[typ], x, y1, maxfev = 500000, p0 = p0type[typ], bounds = bdtype[typ])[0]
	paras = list(paras)

	print('{} Completed'.format(key))
	return lambda x: str2func[typ](x, *paras)


for key in keys:
	if key == 'Population':
		continue

	obj = funcs[key]
	obj['func'] = fitCurve(key)
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
	k, b = (r - l) / 5., l
	thisFunc = (k, b)

	x_res = np.arange(1, 6)
	return func1(x_res, *thisFunc)

df2 = pd.read_excel('raw data backup.xlsx')
df2.index = df2['Year']
df2 = df2.loc[str(start):'2020']

dat_y = [7.76, 8.14, 8.50, 8.84, 9.16, 9.45, 9.73, 9.97, 10.18, 10.38, 10.55, 10.70, 10.84, 10.95, 11.06, 11.14, 11.21]
pop_y = df2['Population'].to_numpy() / (10 ** 9)

for k in range(16):
	qwq = mid_data(dat_y[k], dat_y[k + 1])
	print(qwq)
	pop_y = np.hstack((pop_y, qwq))

df['Population'] = pop_y * 10

print(df.head())
df.to_csv('../single_variable_projection.csv')

sns.set()
cls = sns.hls_palette(10, l=0.7, s=0.4)
fig, ax = plt.subplots(5, 2, figsize = (12, 20))
ax = ax.reshape(10, )
# print(ax)

for k in range(10):
	key = keys[k]
	obj = funcs[key]
	l, r = max(1990, obj['start_year']), 2100
	x = np.arange(l, r + 1)
	y = df[key].loc[str(l):str(r)].to_numpy() / obj['scale']
	print(l, r)

	ax[k].set_title(key)
	ax[k].plot(x, y, color = cls[7], label = 'Predicted {}'.format(key))

	if key != 'Population':
		l2, r2 = obj['start_year'], obj['end_year']
		ori_data = df_origin[key].loc[str(l2):str(r2)].to_numpy()
		x2 = np.arange(l2, r2 + 1)
		ax[k].scatter(x2, ori_data, color = cls[5], s = 5, label = 'Origin {}'.format(key), zorder = 5)

	ax[k].legend()

plt.tight_layout()
# plt.show()
# plt.figure(figsize=(60,1), dpi = 150)
plt.figure(dpi = 150)
# fig.set_size_inches(10.5, 20.5)
# plt.subplots_adjust(hspace=0.3, wspace=0.3)
plt.suptitle('Factors Projection')

# fig.savefig('All Projections.png', dpi=300)