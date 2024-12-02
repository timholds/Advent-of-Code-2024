import numpy as np

data = np.loadtxt('data1.txt', dtype=int)

# we want to sort each list smallest to largest
list1 = np.sort(data[:, 0])
list2 = np.sort(data[:, 1])

# get sum of absolute pairwise distances
sum_sorted_distances = np.sum(np.abs(np.subtract(list1, list2)))
print(sum_sorted_distances)