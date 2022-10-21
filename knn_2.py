import collections

# not using numpy

test = [0, 0, 0]
data = [[1, 1.1, 1.1],[1, 1, 1],[0, 0, 0],[0, 0.1, 0]]
labels = ['A','A','B','B']
k = 2

def get_dist(p1, p2):
    dists = 0
    for i in range(len(p1)):
        dist = (p1[i] - p2[i]) ** 2
        dists += dist
    return dists ** 0.5


def sort_dist(data, test):
    dists = {}
    for i, point in enumerate(data):
        dists[i] = get_dist(test, point)
    sort_key = sorted(dists, key=dists.get)
    return sort_key


def classify(data, test, labels, k):
    sort_key = sort_dist(data, test)
    classes = []
    for i in range(k):
        classes.append(labels[sort_key[i]])
    count = collections.Counter(classes)
    return max(count, key=count.get)
    
        
print(classify(data, test, labels, k))
    

        