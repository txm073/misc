import random
from math import log

def recursive(fn):
    fn.rlevel = 0
    def wrapper(*args, **kwargs):    
        fn.rlevel += 1
        value = fn(*args, **kwargs)
        fn.rlevel -= 1
        return value
    return wrapper

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

def split(arr, n_splits, rlevel=0):
    output = []
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    for arr in [left, right]:
        if not n_splits:
            output.append(arr)
        else:
            output.extend(split(arr, n_splits=n_splits - 1, rlevel=rlevel + 1))
    if not rlevel:
        for i, sublist in enumerate(output):
            if len(sublist) == 2:
                output[i] = [sublist[0], sublist[1]] if sublist[0] <= sublist[1] else [sublist[1], sublist[0]]
    return output
         
def merge_sort(nums, rlevel=0):
    if not rlevel:
        splits = split(nums, n_splits=int(log(len(nums), 2)) - 1)
    else:
        splits = nums
    output = []
    for i in range(0, len(splits), 2):
        output.append(merge(splits[i], splits[i + 1]))
    if len(output) == 1:
        return output[0]
    else:
        return merge_sort(output, rlevel=rlevel + 1)    

if __name__ == "__main__":
    nums = [random.randint(1, 10) for i in range(18)]
    print(nums)
    sort = merge_sort(nums)
    print(sort)
