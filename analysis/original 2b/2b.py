from lib import *

sns.set(style = 'ticks')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']

x1, x2 = np.arange(0, 3), np.arange(3, 6)
a = ['CO2', 'N2O', 'CH4', 'SWDR', 'OLR', 'Sunspots']
y = [0.834, 0.808, 0.807, 0.698, 0.612, 0.596]

a.reverse(); y.reverse()
height = 0.6
plt.barh(x2, y[3:], color = cls[2], height = height, label = 'Greenhouse gases')
plt.barh(x1, y[:3], color = cls[1], height = height, label = 'Solar activities')

plt.xlim(0, 1)
plt.yticks(range(6), a)
# plt.yticklabels(a)
plt.grid(alpha = 0.4)
# plt.show()
plt.legend()
plt.savefig('../original_2b.png', dpi = 300)