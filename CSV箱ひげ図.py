###分散
###


import csv
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, median,variance,stdev
from sklearn import linear_model
import math


temp = []

Vector2 = np.loadtxt('./1VS2.csv', delimiter=',',usecols=1)
Vector3 = np.loadtxt('./1VS3.csv', delimiter=',',usecols=1)
Vector4 = np.loadtxt('./1VS4.csv', delimiter=',',usecols=1)
Vector5 = np.loadtxt('./1VS5.csv', delimiter=',',usecols=1)
Vector6 = np.loadtxt('./1VS6.csv', delimiter=',',usecols=1)
Vector7 = np.loadtxt('./1VS7.csv', delimiter=',',usecols=1)
Vector8 = np.loadtxt('./1VS8.csv', delimiter=',',usecols=1)
Vector9 = np.loadtxt('./1VS9.csv', delimiter=',',usecols=1)
Vector10 = np.loadtxt('./1VS10.csv', delimiter=',',usecols=1)
Vectors = [temp,temp,Vector2,Vector3,Vector4,Vector5,Vector6]
vector = [[0 for i in range(10)] for j in range(len(Vectors))]
means = [0 for i in range(len(Vectors)-2)]


for numv in range(10):
    for numV in range(len(Vectors)):
        if numV<2:
            continue
        if numV == 5:
            vector[numV][numv] = (Vectors[5][2*numv+1])
        else :
            vector[numV][numv] = (Vectors[numV][2*numv])

points = (vector[2],vector[3],vector[4],vector[5],vector[6])

#plt.figure() ##箱ひげ図
fig, ax = plt.subplots() 
bp = ax.boxplot(points) # 複数指定する場合はタプル型で渡します。
left = ['+1','+2','+3','+4','+5']
left003 = [1,2,3,4,5]
ax.set_xticklabels(left)

plt.title('Difference in the number of cards')
plt.grid() # 横線ラインを入れることができます。


for num in range (len(Vectors)):
    if num < 2:
        continue
    m = mean(vector[num])
    means[num-2] = m
    md = median(vector[num])
    v = variance(vector[num])
    s= stdev(vector[num])
    print('平均: {0:.2f}'.format(m))
    print('中央値: {0:.2f}'.format(md))
    print('分散: {0:.2f}'.format(v))
    print('標準偏差: {0:.2f}'.format(s))
print(means)

#plt.figure() ##平均値の折れ線グラフ
plt.plot(left003,means)

left002 = [[1],
           [2],
           [3],
           [4],
           [5]]


model = linear_model.LinearRegression()
#model_lr = LinearRegression()
model.fit(left002, means)
R2 = model.score(left002,means)
print(R2)
print(math.sqrt(R2))
plt.plot(left002,model.predict(left002), 'g')#linestyle ='solid'#回帰直線
print(model.coef_)



# 描画
plt.show() 