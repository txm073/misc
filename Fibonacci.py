import re

calc = input()
fib_search = re.search("fib\([0-9]+\)",calc)
if fib_search:
    times = int(calc[4:-1])
nums = [0,1]
for i in range(times):
    nums.insert(i+2,(nums[i]+nums[i+1]))
print(f"The {times} term in the Fibonacci sequence is {nums[times-1]}")
print(str(nums[:-2])[1:-1])