import time

i = 0
while True:
    i += 1
    time.sleep(1)
    print(i, end="\r")