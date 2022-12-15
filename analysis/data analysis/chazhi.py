from lib import *
from sklearn.metrics import r2_score


df = pd.read_excel('shortwave.xlsx')
print(df)
sns.set()

def f(x, p2, p3, p4, p5, p6, p7, p8):
	# p4 = 2 * math.pi / 10
	# p7 = 2 * math.pi / 12
	# p10 = 2 * math.pi / 11
	return p2 + p3*np.sin(p4*x + p5) + p6*np.sin(p7*x + p8)

p0 = [1 for i in range(7)]
bd = (-np.inf, np.inf)

x = df['X'].to_numpy()
y = df['Y'].to_numpy()

def _uniform(y):
	c = np.max(y) - np.min(y)
	y = (y - np.min(y)) / c
	return y

# y = _uniform(y)
print(y)

paras = optimize.curve_fit(f, x, y, maxfev = 2 * 10 ** 9, p0 = p0, bounds = bd)[0]
paras = list(paras)
# print(paras)
for i in paras:
	print('%.2f'%i)
func = lambda x: f(x, *paras)

r2 = r2_score(y, func(x))
print('R square = {}'.format(r2))

x2 = np.linspace(0, 100, 100)
plt.plot(x, y)
plt.plot(x2, func(x2))
plt.show()