from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

import numpy as np

data = []

def set_data():
    filename = input("- input file name: ")
    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line: break
        point = line.split(",")
        data.append([float(point[0]), float(point[1])])

def hierachical_clustering():
    Z = hierarchy.linkage(X, 'single')

    return Z

def set_dendrogram(Z):
    dn = hierarchy.dendrogram(Z)

    hierarchy.set_link_color_palette(['m', 'c', 'y', 'g', 'k'])
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='b', orientation='top')
    dn2 = hierarchy.dendrogram(Z, ax=axes[1], above_threshold_color='#000000', orientation='right')
    hierarchy.set_link_color_palette(None)

if __name__ == "__main__":
    set_data()
    X = np.array(data)

    Z = hierachical_clustering()
    set_dendrogram(Z)
    plt.show()
