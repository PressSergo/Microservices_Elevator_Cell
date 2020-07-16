import random
import pymongo

# myclient = pymongo.MongoClient("mongodb://192.168.99.100:27017/", username='admine', password='admine')
# mydb = myclient["Elevator"]
# mycol = mydb["CellsElevator"]
#
# mylist = []
#
# for i in range(0,130):
#     mylist.append({"f1": str(random.randint(0,20)), "f2": str(random.randint(0,20)),"time":str(random.randint(0,12))},)
#
# for i in range(0,130):
#     mylist.append({"f1": str(random.randint(0,3)), "f2": str(random.randint(0,20)),"time":str(random.randint(6,9))},)
#
# x = mycol.insert_many(mylist)
#
# # print list of the _id values of the inserted documents:
# print(x.inserted_ids)


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# read data (drop last empty column, caused by an extra (last) colon in the header)
data = pd.read_csv("CellsElevator.csv", sep=',')

# # normalize data
# scaler = StandardScaler()
# X = scaler.fit_transform(data.drop('Пользователь', 1))

print(data[['f1','f2','time']])

plt.scatter(data[['f1']],data[['time']])
plt.xlabel("Время")
plt.ylabel("Этаж вызова")
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(data[['f1','time']])

plt.scatter(data[['f1']],data[['time']])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.xlabel("Время")
plt.ylabel("Этаж вызова")
plt.show()

print(kmeans.predict([[15,2]]))
print(kmeans.predict([[0,6]]))
print(kmeans.predict([[15,10]]))