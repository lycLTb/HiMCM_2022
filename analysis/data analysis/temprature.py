from lib import *
from sklearn.metrics import r2_score
import statsmodels.api as sm

df = pd.read_excel('problem2_data.xlsx')
l, r = 1958, 2021
print(df)

sns.set(style = 'ticks')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']



def f(x, p1, p2, p3, p5, p6, p8, p9, p11):
	p4 = 2 * math.pi / 10
	p7 = 2 * math.pi / 12
	p10 = 2 * math.pi / 11
	return p1*x + p2 + p3*np.sin(p4*x + p5) + p6*np.sin(p7*x + p8) + p9*np.sin(p10*x + p11)
# exit(0)

p0 = [1 for i in range(8)]
bd = (-np.inf, np.inf)

x = np.arange(0, r - l + 1)
y = df['Degrees C'].to_numpy()

lowess = sm.nonparametric.lowess
# plt.plot(x, y, color = cls[0])
# for i in range(1, 4):
# 	result = lowess(y, x, frac = i / 10., it = 3, delta = 0.)
# 	plt.plot(x, result[...,1], color = cls[i * 3])
# plt.show()

result = lowess(y, x, frac = 0.15, it = 3, delta = 0.)[...,1]

paras = optimize.curve_fit(f, x, result, maxfev = 5000000, p0 = p0, bounds = bd)[0]
paras = list(paras)
func = lambda x: f(x, *paras)
print(paras)

def getFirst():
	bound = [1.25, 1.5, 2.]
	got = [False, False, False]
	first = [0, 0, 0]

	xx = np.arange(l, r + 80)
	yy = func(xx - l)
	for i in range(r + 80 - l):
		for j in range(3):
			if yy[i] >= bound[j] and not got[j]:
				got[j] = True
				first[j] = xx[i]

	return first

def drawPoint(x, y, notation, label = None):
	xr = (x - plt.xlim()[0]) / (plt.xlim()[1] - plt.xlim()[0])
	yr = (y - plt.ylim()[0]) / (plt.ylim()[1] - plt.ylim()[0])
	plt.axhline(y = y, xmax = xr, color = cls[3], ls = notation, linewidth = 1.5)
	plt.axvline(x = x, ymax = yr, color = cls[3], ls = notation, linewidth = 1.5)
	plt.scatter(x, y, color = cls[6], s = 20, label = label, zorder = 5)

def plotDashedLine():
	bound = [1.25, 1.5, 2]
	first = getFirst()

	for i in range(3):
		drawPoint(first[i], bound[i], '--', label = '{}, {}°C'.format(first[i], bound[i]))

def Plot():
	x_plot = np.linspace(l, r + 80, 500)
	y_plot = func(x_plot - l)

	r2 = r2_score(y, func(x))
	print('R square = {}'.format(r2))

	plt.plot(x + l, y, label = 'Raw data', color = cls[3])
	plt.plot(x + l, result, label = 'Smoothened data', color = cls[2], linewidth = 2)
	# plt.plot(x_plot, y_plot, label = 'Fitted Curve', color = cls[3], linewidth = 2)
	# plt.title('Temprature Projection with Lowess Smoothing')
	# plotDashedLine()

	plt.xlabel('Year')
	plt.ylabel('Relative Temprature / °C')
	plt.legend()
	# plt.show()
	# plt.savefig('../2a_prediction.png', dpi = 300)
	plt.savefig('../Lowess.png', dpi = 300)

def ExportData():
	xx = np.arange(l, 2101)
	yy = func(xx - l)
	dfo = pd.DataFrame(np.vstack((xx, yy)).T)
	dfo.to_csv('../2a.csv')

Plot()
ExportData()