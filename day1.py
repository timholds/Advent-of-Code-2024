import numpy as np
from collections import defaultdict

# Part 1:
data = np.loadtxt('data1.txt', dtype=int)

# we want to sort each list smallest to largest
list1 = np.sort(data[:, 0])
list2 = np.sort(data[:, 1])

# dummy data
# list1 = np.array([1, 2, 3, 4, 3])
# list2 = np.array([1, 3, 3, 3, 8])

# get sum of absolute pairwise distances
sum_sorted_distances = np.sum(np.abs(np.subtract(list1, list2)))
print(f'Answer to part 1: {sum_sorted_distances}')




# Part 2: how often do items from list 1 occur in list 2
intersection = np.intersect1d(list1, list2)
num_overlapping = len(intersection)
# print(f'num_overlapping {num_overlapping} out of {len(list1)}') # sanity check


# every number not in the intersection will have a score of 0
# for each num in intersection, we could do num * occur in list1 * occur list2
s = []
for unique_num in intersection:
    occur_list1 = np.count_nonzero(list1 == unique_num)
    occur_list2 = np.count_nonzero(list2 == unique_num)
    score = unique_num * occur_list1 * occur_list2
    # print(unique_num, occur_list1, occur_list2, score)
    s.append(score)

print(f'Answer to part 2: {sum(s)}')

