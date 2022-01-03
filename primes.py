import sys
import time

def timed(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = fn(*args, **kwargs)
        time_taken = time.time() - start
        return return_value, time_taken
    return wrapper

@timed
def get_primes(n):
    primes = []
    for i in range(1, n):
        factors = [j for j in range(1, i+1) if i % j == 0]
        if len(factors) == 2:
            primes.append(i)
    return primes

@timed
def get_primes_faster(n, method="up_to"):
    def ngen():
        j = 2
        while True:
            yield j
            j += 1

    def primegen(gen):
        num = next(gen)
        yield num
        yield from primegen((i for i in gen if i % num != 0))   

    if n > 1000:
        sys.setrecursionlimit(n)

    pgen = primegen(ngen())
    if method == "up_to":
        primes = []
        i = next(pgen)
        while i < n:
            primes.append(i)
            i = next(pgen)
        return primes
    
    return [next(pgen) for i in range(n)]


print(get_primes_faster(500, method="n_primes")[1])
#print(get_primes(10000)[1])
