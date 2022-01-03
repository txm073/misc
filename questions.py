import random
import threading
import time

rounds = 10
score = 0
finished = False

def timer():
    start = time.time()
    while not finished:
        pass
    global time_taken
    time_taken = time.time() - start

thread = threading.Thread(target=timer).start()
operators = {0: "+", 1: "-", 2: "*", 3: "/"}
nums = [random.randint(1, 100) for i in range(rounds * 2)]
for i in range(0, len(nums), 2):
    op = operators[(i // 2) % 4]
    ans = eval(str(nums[i]) + op + str(nums[i + 1]))
    inp = input(f"What is {nums[i]} {op} {nums[i + 1]}? ")
    while True:
        try:
            int(inp)
            break
        except ValueError:
            inp = input(f"What is {nums[i]} {op} {nums[i + 1]}? ")
    if int(inp) == ans:
        score += 1    

finished = True
time.sleep(0.5)
print(f"You got {score} / {rounds} answers correct in {time_taken:2f} seconds!")