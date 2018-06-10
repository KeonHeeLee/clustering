from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import numpy as np


data = []

def set_data():
    filename = input("input file name: ")
    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line: break
        point = line.split(",")
        data.append([float(point[0]), float(point[1])])

def agglomerative(X):
    import time
    start_time = time.time()

    agg = AgglomerativeClustering(n_clusters=5)
    assignment = agg.fit(X=X)

    print("%s seconds ---" % (time.time() - start_time))
    plt.scatter(X[:, 0], X[:, 1], c=agg.labels_, cmap='rainbow')


if __name__ == "__main__":
    set_data()
    X = np.array(data)

    agglomerative(X=X)

    plt.show()
