###分散出します


import csv
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, median,variance,stdev

# CSVファイルの読み込み
#csv_file = open("./.csv", "r", encoding="ms932", errors="", newline="" )


temp = []

Vector2 = np.loadtxt('./1VS2.csv', delimiter=',',usecols=1)
Vector3 = np.loadtxt('./1VS3.csv', delimiter=',',usecols=1)
Vector4 = np.loadtxt('./1VS4.csv', delimiter=',',usecols=1)
Vector5 = np.loadtxt('./1VS5.csv', delimiter=',',usecols=1)
Vector6 = np.loadtxt('./1VS6.csv', delimiter=',',usecols=1)
Vector7 = np.loadtxt('./1VS7.csv', delimiter=',',usecols=1)
Vectors = [temp,temp,Vector2,Vector3,Vector4,Vector5,Vector6,Vector7]
vector = [[0 for i in range(10)] for j in range(len(Vectors))]



for numv in range(10):
    for numV in range(len(Vectors)):
        if numV<2:
            continue
        if numV == 5:
            vector[numV][numv] = (Vectors[5][2*numv+1])
        else :
            vector[numV][numv] = (Vectors[numV][2*numv])

points = (vector[2],vector[3],vector[4],vector[5],vector[6],vector[7])

fig, ax = plt.subplots() 
bp = ax.boxplot(points) # 複数指定する場合はタプル型で渡します。
ax.set_xticklabels(['+1', '+2','+3','+4','+5','+6'])
plt.title('Difference in the number of cards')
plt.grid() # 横線ラインを入れることができます。
 
# 描画
plt.show() 




for num in range (len(Vectors)):
    if num < 2:
        continue
    m = mean(vector[num])
    md = median(vector[num])
    v = variance(vector[num])
    s= stdev(vector[num])
    print('平均: {0:.2f}'.format(m))
    print('中央値: {0:.2f}'.format(md))
    print('分散: {0:.2f}'.format(v))
    print('標準偏差: {0:.2f}'.format(s))





