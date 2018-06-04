import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

data = []

def set_data():
    filename = input("- input file name: ")
    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line: break
        point = line.split(",")
        data.append([float(point[0]), float(point[1])])

def set_DBSCAN(eps, min_sample):
    db = DBSCAN(eps=eps, min_samples=min_sample)
    db.fit(X)

    return db


if __name__ == "__main__":
    set_data()
    X = np.array(data)

    eps        = int(input("- input eps        :"))
    min_sample = int(input("- input min_sample :"))

    db = set_DBSCAN(eps=eps, min_sample=min_sample)
    plt.scatter(X[:, 0], X[:, 1], c=db.labels_, cmap='rainbow')
    plt.show()
