import numpy as np
from matplotlib import pyplot as plt
import random
import pandas as pd

list1 =[]
list2 =[]
for random_num in range(100):
    list1.append(random.randint(1, 101))
    list2.append(random.randint(1, 1001))

plt.scatter(list1,list2,color='black')
plt.show()
df = pd.DataFrame({'firstlist': list1,
                   'secondlist': list2},
                  columns=['firstlist', 'secondlist'])
df['split'] = np.random.randn(df.shape[0], 1)
df['split2'] = np.random.randn(100, 1)
print(df.shape)
print(df.shape[0])

msk = np.random.rand(len(df)) <= 0.8
print(msk)
train1 = df[msk]
test1 = df[~msk]
print(train1.head())
print(test1.head())
print(train1.shape)
print(test1.shape)
print(len(df))


X = df['firstlist'].values
Y = df['secondlist'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
print(mean_x, mean_y)
n = len(X)
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
    m = numer / denom
    c = mean_y - (m * mean_x)

# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x

# Ploting Line
plt.plot(x, y, color='black', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='green', label='Scatter Plot')

plt.xlabel('First List')
plt.ylabel('Second List')
plt.legend()
plt.show()
