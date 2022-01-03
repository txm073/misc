import random


def quicksort(nums):
    pivot = nums[len(nums) // 2]
    del nums[len(nums) // 2]
    nums.append(pivot)
    while True:
        for left in range(0, len(nums), 1):
            if nums[left] > pivot:
                break
        for right in range(len(nums) - 1, -1, -1):
            if nums[right] < pivot:
                break
        if right < left:
            nums[right], nums[left] = nums[left], nums[right]
        elif left > right:
            nums[-1], nums[left] = nums[left], nums[-1]
            break
    return nums

nums = [random.randint(1, 10) for i in range(10)]
print(nums)
sort = quicksort(nums)
print(nums)