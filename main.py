import pandas as pd
import numpy as np

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
#
# c = a + b
# print(c)
# d = np.sqrt(b)
# print(d)
#
# e = d + c
# print(e)

# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))

# a = np.arange(3)
# b = np.arange(3)
# print(np.dot(a, b))
# print(a.dot(b))
# c = np.arange(3)
# d = np.array([[0], [1], [2]])
# print(c.dot(d))
# e = np.array([[2, 4, 5], [5, 1, 7]])
# f = np.array([[2, 3], [4, 2], [6, 1]])
# print(np.dot(e, f))

# a = np.arange(6).reshape((3, 2))
# print(a)
# print(a.flat)
# for b in a.flat:
#     print(b)
# print("!!!!!!!!!!!!!!!!!!")
# for b in a:
#     for c in b:
#         print(c)

# a = np.arange(12).reshape((3, 4))
# print(a)
# b = a.reshape((4, 3))
# print(b)
# c = b.ravel()
# print(c)
# print(b.T)

# s = pd.Series([1, 3, 5, 'a', 5.5])
# print(s)
s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [111908846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
#
# daty = pd.date_range('20220507', periods=5)
# print(daty)
# df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df2)
#
# df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df3)
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# print(df.head(10))
# print(df.tail(10))
#
# df3.to_csv('dane2.csv', index=False)
# df.to_excel('imiona2.xlsx', sheet_name='dane')

print(s['a'])
print(s.a)

print(df[0:1])

print(df['Kraj'])
print(df.Kraj)

print(df.iloc[0], [0])
print(df.loc[[0], ['Kraj']])
print(df.at[0, 'Kraj'])
