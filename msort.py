import random
from math import log

def merge(list1, list2):
    output = []
    for i in range(len(list1) + len(list2)):
        if (list1 and not list2) or (list2 and not list1):
            output.append((list1 or list2)[0])
            del (list1 or list2)[0]
            continue
        if list1[0] <= list2[0]:
            output.append(list1[0])
            del list1[0]
        elif list1[0] >= list2[0]:
            output.append(list2[0])
            del list2[0]
    return output

def split(arr, n_splits):
    output = []
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    for arr in [left, right]:
        if not n_splits:
            output.append(arr)
        else:
            output.extend(split(merge(*split(arr, n_splits=n_splits - 1)), n_splits=n_splits - 1))
    return output
        
def merge_sort(nums):
    nums = split(nums)
    for iteration in range(log(len(nums), 2)):
        pass

nums = [random.randint(1, 10) for i in range(35)]
print(nums)
sort = split(nums, int(log(len(nums), 2)) - 1)
print(sort)
print(sum([len(sublist) for sublist in sort]))

