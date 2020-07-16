import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
#
X1= [random.randint(0,90) for i in range(0,50)]
Y1 = [random.randint(0,90) for i in range(0,50)]
w = [random.randint(0,12) for i in range(0,50)]

mst = []
mst.append(X1)
mst.append(Y1)
mst.append(w)

# X, y = make_blobs(n_samples=10, centers=None, n_features=4, random_state=2)

plt.scatter(mst[0], mst[1])
plt.show()

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(mst)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(mst)
plt.show()

plt.scatter(mst[:,0], mst[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()

print(mst)
print(mst[:,0])
print(mst[:,1])
#
# plt.scatter(X1,Y1, marker = "o")
# plt.grid()
# plt.legend()
# plt.show()
#
# # Описываем модель
# model = KMeans(n_clusters=3)
