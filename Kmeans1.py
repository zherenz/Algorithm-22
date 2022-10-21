import numpy as np
import copy

def dist1(p1, p2):
    return np.linalg.norm(p1 - p2, axis=1)


def dist2(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def dist3(p1, p2):
    dist_sum = 0
    for i in range(len(p1)):
        dist = (p1[i] - p2[i]) ** 2
        dist_sum += dist
    return np.sqrt(dist_sum)
        

data = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9,11], [2, 1], [7, 2], [6, 9], [3, 3], [7, 1], [10, 2], [2, 8]])
k = 3
C_x = np.random.randint(0, np.max(data) - 3, size=k)
C_y = np.random.randint(0, np.max(data) - 3, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)

C_old = np.zeros(C.shape)
cluster_of_point = np.zeros(len(data))
iteration_flag = dist1(C, C_old)
itr = 1

while iteration_flag.any() != 0 and itr < 2:
    
    for i in range(len(data)):
        distances = dist1(data[i], C)
        cluster = np.argmin(distances)
        cluster_of_point[i] = cluster
        
    C_old = copy.deepcopy(C)
    for i in range(k):
        points = []
        for j in range(len(data)):
            if cluster_of_point[j] == i:
                points.append(data[j])
        # points = [data[j] for j in range(len(data)) if cluster_of_point[j] == i]
        # print(points)
        # print(np.mean(points, axis=0))
        C[i] = np.mean(points, axis=0)

    print ('itr: %d' % itr)
    itr = itr + 1
    iteration_flag = dist1(C, C_old)
    print("distance: ", iteration_flag)