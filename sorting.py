"""Sorting algorithms implementated in Python"""

import random
from math import log
from time import perf_counter

# NOTE Parameter `rlevel` is used in functions to track the current recursion level
# Do not modify that parameter and create a wrapper if you do not want it

def timed(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = fn(*args, **kwargs)
        return value, perf_counter() - start
    return wrapper

@timed
def bubble_sort(nums):
    """Bubble sort algorithm - between O(n) and O(n ^ 2) - least efficient"""
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            try:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j] 
            except IndexError:
                continue
    return nums

@timed
def insertion_sort(nums):
    """Insertion sort algorithm - between O(n) and O(n ^ 2) - most efficient for small arrays"""
    for i in range(len(nums)):
        while i >= 1 and nums[i - 1] > nums[i]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums

@timed
def pivot_sort(nums):
    """Pivot sort algorithm - between O(n * log n) and O(n ^ 2) - most efficient overall"""
    while True:
        pivot_value = nums[len(nums) // 2]
        left, right = 0, len(nums) - 1
        while nums[left] < pivot_value:
            left += 1
        while nums[right] > pivot_value:
            right -= 1
        print(left, right)
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
        if left + 1 == right - 1:
            break
        break
    return nums

@timed
def merge_sort(nums):
    """Merge sort algorithm - between O(n ^ log n) and O(n ^ 2)"""

    def merge(list1, list2):
        """Merge two lists of the same length or 1 element difference in length"""
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
        """Split into sublists by recursively splitting a certain number of times"""
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
            
    def _merge_sort(nums, rlevel=0):
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
            return _merge_sort(output, rlevel=rlevel + 1)  

    return _merge_sort(nums, 0)


if __name__ == "__main__":
    nums = [random.randint(1, 1000) for i in range(500000)]
    sort = merge_sort(nums)
    print(sort[1])