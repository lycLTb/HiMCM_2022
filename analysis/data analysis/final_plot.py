from lib import *

df = pd.read_csv('../result.csv')
df.index = df.iloc[...,0].to_numpy()
df = df.drop('Unnamed: 0', axis = 1)
df = df.T

x = df.index.to_numpy()
for i in range(101):
	x[i] = int(x[i])


df_ori = pd.read_excel('../himcm_origin_data.xlsx')
df_ori.index = df_ori.iloc[...,0].to_numpy()
df_ori = df_ori.drop('Year', axis = 1)
df_ori = df_ori.loc['2000':'2021'].to_numpy()
# print(df_ori)

sns.set(style = 'whitegrid')
cls = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2', '#999999']
plt.plot(x, df['Model 1'].to_numpy(), label = 'Model 1', color = cls[0], linewidth = 2)
plt.plot(x, df['Model 2'].to_numpy(), label = 'Model 2', color = cls[4], linewidth = 2)
plt.plot(x, df['Model 3'].to_numpy(), label = 'Model 3', color = cls[3], linewidth = 2)
plt.scatter(np.arange(2000, 2022), df_ori, label = 'Past data', color = cls[2], s = 10, zorder = 5, marker = 'x')

# plt.title('General CO2 Concentration Projections')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration / PPM')
plt.legend()
plt.savefig('General Projections.png', dpi=300)
plt.show()