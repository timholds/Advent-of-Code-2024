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
df['safe'] = False
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
# add a column that determines whether it is safe or unsafe 
for i, report in enumerate(df.values):
    # report[0] gets the string '38 41 44 47 50 47' out of array
    # report[0].split() will break up the string by whitespace 
    # breakpoint()
    numbers = np.array(report[0].split(), dtype=int)
    safe_value = row_is_decreasing_safe(numbers) or row_is_increasing_safe(numbers)
    if safe_value == True:
    #     print(numbers, 'safe!')
        safe +=1 
    # else:
    #     print(numbers, 'NOT safe')
    #     print(row_is_decreasing_safe(numbers))
    #     print(row_is_increasing_safe(numbers))

    # breakpoint()
    df.loc[i, 'safe'] = safe_value

print(f'solution to part 1 is: {safe}')
print(df)
# count number of entries that are true in df
num_safe_entries = (df['safe'] == True).sum()
print(num_safe_entries)


## PART 2
# for reports that are unsafe, check if there is a singe
# entry change that wouldmake it work

# TODO try actually removing the element from the array

unsafe_entries = df['safe'] == False
print(df[unsafe_entries])

def row_is_inc_fuzzy_safe(arr):
    low = 0
    high = 1
    remove_count = 0
    while high < len(arr):
        diff = arr[high] - arr[low]

        if diff > 3:
            high += 1    
            remove_count +=1 
            # its already sorted incresing we are assuming
            # if the diff already >3, increasing high won't help us 
            # maybe increase low and high and assume we are dropping low

        elif diff < 1:
            arr = np.delete(arr, low)
            remove_count +=1 
        else: # within valid range, increse both 
            low +=1 
            high += 1

        if remove_count > 1:
            #print(f'arr is NOT fuzzy safe: {arr}')
            return False

    print(f'arr is fuzzy safe inc: {arr}, remove_count {remove_count}')
    return True


def row_is_dec_fuzzy_safe(arr):
    # print(f'checking {arr}')
    # check if its increasing by 1 or two
    remove_count = 0
    low = 0
    high = 1

    while high < len(arr):
        diff = arr[low] - arr[high]
        print(f'low {low}, high {high}, {arr[low]} - {arr[high]} =  diff {diff}')
        if diff > 3:
            print('diff larger than 3')
            if high + 1 < len(arr):
                new_diff = arr[low] - arr[high+1]
                if new_diff <= 3 and new_diff >= 1: 
                    print(f'removing item at high {arr[high]}')
                    remove_count +=1
                    high += 2
                    low += 1

                else:
                    print('dropping 1 does not fix issue')
                    return False
            else:
                remove_count += 1
        elif diff < 1:
            print('diff smaller than 1')
            # try low - 1
            new_diff = arr[low-1] - arr[high]
            print(f'low-1 {low-1}, high {high}, {arr[low-1]} - {arr[high]} =  diff {diff} diff {new_diff}')
            if new_diff <= 3 and new_diff >= 1: 
                print(f'removing item at low {arr[low]}')
                remove_count +=1
                low += 1
                high += 1


            else:
                print('moving up or down 1 doesnt fix issue')
                return False
            #high +=1
        else:
            low += 1 
            high += 1

        if remove_count > 1:
            print(f'arr is NOT fuzzy safe: {arr}, remove_count {remove_count}')
            return False
    
    print(f'arr is fuzzy safe dec: {arr}, remove_count {remove_count}')
    return True
   
#  check the unsafe reports to see if they are almost safe
for i, report in enumerate(df[unsafe_entries].values):
    # report[0] gets the string '38 41 44 47 50 47' out of array
    # report[0].split() will break up the string by whitespace 
    # breakpoint()
    # safe = 0
    numbers = np.array(report[0].split(), dtype=int)

    safe_value = row_is_dec_fuzzy_safe(numbers) or row_is_inc_fuzzy_safe(numbers)
    # if safe_value == True:
    # #     print(numbers, 'safe!')
    #     safe +=1 
    # # else:
    # #     print(numbers, 'NOT safe')
    # #     print(row_is_decreasing_safe(numbers))
    # #     print(row_is_increasing_safe(numbers))

    # breakpoint()
    # update dataframe safe column to include those that are fuzzy safe
    df.loc[i, 'safe'] = safe_value

num_fuzzy_safe_entries = (df['safe'] == True).sum()
print(f'Answewr Part 2: {num_fuzzy_safe_entries}')