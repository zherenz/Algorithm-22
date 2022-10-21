import numpy as np

centers = [[1, 3], [4, 8], [7, 2]]
dataset = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9,11], [2, 1], [7, 2], [6, 9], [3, 3], [7, 1], [10, 2], [2, 8]]

clusters = {}
for data in dataset:
    dists = []
    for center in centers:
        dist_sum = 0
        for i in range(len(data)):
            dist = (data[i] - center[i]) ** 2
            dist_sum += dist
        dists.append(dist_sum ** 0.5)
    cluster_blgs_to = np.argmin(dists)
    clusters[cluster_blgs_to].append(data)
    
centers_old = centers.copy()
centers = [np.mean(cluster, axis=0) for cluster in clusters]
    
    
