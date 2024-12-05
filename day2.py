## PART 1
# a report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# consists of many reports, one report per line. Each report is a list of numbers called levels

# determine if the level is increasing or decreasing
# make sure that the increase/decrease is within the expected range

# read in the data from data/data2.txt
import numpy as np
import pandas as pd
df = pd.read_csv('data/data2.txt', header=None)

# are we guaranteed at least two items in every row

def row_is_increasing_safe(arr):
    # check if its increasing by 1 or two
    # print(f'checking {arr}')
    idx = 1
    while idx < len(arr):
        if arr[idx] - arr[idx-1] > 3:
            return False # too big of an increase
        elif arr[idx] - arr[idx-1] < 1:
            return False # too small of an increase
        idx += 1
    return True

def row_is_decreasing_safe(arr):
    # print(f'checking {arr}')
    # check if its increasing by 1 or two
    idx = 1
    while idx < len(arr):
        if arr[idx-1] - arr[idx] > 3:
            return False # decreasing too fast
        elif arr[idx-1] - arr[idx] < 1:
            return False
        idx +=1
    return True
    

safe = 0
# iterative solution
for report in df.values:
    # report[0] gets the string '38 41 44 47 50 47' out of array
    # report[0].split() will break up the string by whitespace 
    # breakpoint()
    numbers = np.array(report[0].split(), dtype=int)
    if row_is_decreasing_safe(numbers) or row_is_increasing_safe(numbers):
        print(numbers, 'safe!')
        safe +=1 
    else:
        print(numbers, 'NOT safe')
        print(row_is_decreasing_safe(numbers))
        print(row_is_increasing_safe(numbers))

print(f'solution to part 1 is: {safe}')


## PART 2


# def row_is_valid(df):
#     # get a list from the row data
    
# df['valid'] = df.apply(row_is_valid, axis=1)

# for each row in the df, determine if its valid or not and count total number of valid
# import pdb; pdb.set_trace()

# data = []
# with open('data/data2.txt', 'r') as file:
#     for line in file:
#         # Convert each line to list of integers, skipping any empty lines
#         if line.strip():
#             numbers = list(map(int, line.strip().split()))
#             data.append(numbers)