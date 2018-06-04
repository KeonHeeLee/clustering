import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = []

def set_data():
    filename = input("input file name: ")
    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line: break
        point = line.split(" ")
        data.append([float(point[0]), float(point[1])])

def k_means(X):
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)

    print(kmeans.cluster_centers_)
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')

if __name__ == "__main__":
    set_data()
    X = np.array(data)

    k_means(X=X)

    plt.show()
