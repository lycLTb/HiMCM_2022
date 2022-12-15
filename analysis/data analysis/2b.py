from lib import *

df = pd.read_excel('../2b.xlsx')
df.index = df.iloc[...,0].to_numpy()
df = df.drop('Unnamed: 0', axis = 1)
# print(df)
tmp = df.corr(method = 'spearman')
# print(tmp[0, 0])

l, r = 1959, 2100
le, re = 8, 8

res = []
for i in range(l + le, r - re + 1):
	L, R = i - le, i + re
	dff = df.loc[L:R]
	res.append(dff.corr(method = 'spearman').iloc[:3, 3])

x = np.arange(l + le, r - re + 1)
res = np.array(res).T
print(res)

sns.set(style = 'ticks')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']

plt.plot(x, res[0], label = 'Model 1', color = cls[0])
plt.plot(x, res[1], label = 'Model 2', color = cls[1])
plt.plot(x, res[2], label = 'Model 3', color = cls[2])
plt.axhline(y = 0, color = cls[6], zorder = 0, ls = '--')

plt.xlabel('Year')
plt.ylabel("Spearman's Coefficient")
plt.legend()
# plt.show()
plt.savefig('../2b.png', dpi = 300)