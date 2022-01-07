"""Merge sort algorithm implementation in Python"""

import random
from math import log

# NOTE Parameter `rlevel` is used in functions to track the current recursion level
# Do not modify that parameter and create a wrapper if you do not want it

def merge(list1, list2):
    """Merge two lists of the same length or 1 element difference in length"""
    output = []
    # Repeat for all elements in both lists
    for i in range(len(list1) + len(list2)):
        # If one of the lists have 1 element and the other one has 0 elements
        if (list1 and not list2) or (list2 and not list1):
            output.append((list1 or list2)[0])
            del (list1 or list2)[0]
            continue
        # Append lower of the compared values
        if list1[0] <= list2[0]:
            output.append(list1[0])
            del list1[0]
        elif list1[0] >= list2[0]:
            output.append(list2[0])
            del list2[0]
    return output

def split(arr, n_splits, rlevel=0):
    """Split into sublists by recursively splitting a certain number of times"""
    output = []
    # Split array into two halves
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    for arr in [left, right]:
        # If array has been splitted enough times
        if not n_splits:
            output.append(arr)
        # Split again
        else:
            output.extend(split(arr, n_splits=n_splits - 1, rlevel=rlevel + 1))
    if not rlevel:
        # Rearrange sublists that contain 2 elements otherwise the merge sort will not work
        for i, sublist in enumerate(output):
            if len(sublist) == 2:
                output[i] = [sublist[0], sublist[1]] if sublist[0] <= sublist[1] else [sublist[1], sublist[0]]
    return output
         
def merge_sort(nums, rlevel=0):
    """Use the merge sort algorithm to sort an unordered list of numbers"""
    # First level of recursion
    if not rlevel:
        # Split the list: logarithm with base 2 to determine the number of times to split
        splits = split(nums, n_splits=int(log(len(nums), base=2)) - 1)
    else:
        splits = nums
    output = []
    for i in range(0, len(splits), 2):
        output.append(merge(splits[i], splits[i + 1]))
    # Check if the output has 1 sublist
    if len(output) == 1:
        return output[0]
    # Otherwise sublists again
    else:
        return merge_sort(output, rlevel=rlevel + 1)    


if __name__ == "__main__":
    nums = [random.randint(1, 10) for i in range(18)]
    print(nums)
    sort = merge_sort(nums)
    print(sort)