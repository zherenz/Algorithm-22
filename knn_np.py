import numpy as np
import collections

# KNN1
# all inputs are in numpy array format, using numpy in functions

def create_dataset():
    data = np.array([[1, 1.1, 1.1],[1, 1, 1],[0, 0, 0],[0, 0.1, 0]])
    labels = np.array(['A','A','B','B'])
    return data, labels


def classify(testdata, data, labels, k):
    test_tile = np.tile(testdata, (len(data), 1))
    sq_dist_matrix = (test_tile - data) ** 2
    sq_dist = np.sum(sq_dist_matrix, axis=1)  # (n, 1)
    dist = np.sqrt(sq_dist)
    nearest = np.argsort(dist)
    
    label_set = set(labels)
    label_dict = {key: 0 for key in label_set}
    for i in range(k):
        label = labels[nearest[i]]
        label_dict[label] += 1
    pred = max(label_dict, key=label_dict.get)
    return pred


def classify_short(testdata, data, labels, k):
    dist = np.sqrt([sum((single_data - testdata) ** 2) for single_data in data])
    # dist = []
    # for single_data in data:
    #     dist.append(dist3(single_data, testdata))
        
    nearest = np.argsort(dist)
    topk = [labels[nearest[i]] for i in range(k)]
    topk_count = collections.Counter(topk)
    pred = max(topk_count, key=topk_count.get)
    return pred    
    

def main(): 
    data, labels = create_dataset()
    pred = classify(np.array([0, 0, 0]), data, labels, 3)
    pred_2 = classify_short([0, 0, 0], data, labels, 3)
    print(pred)
    print(pred_2)
    

if __name__ == "__main__":
    main()
    
    
    
    