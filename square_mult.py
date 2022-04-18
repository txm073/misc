import time

def square_mult(base, exp, mod=None):
    n = 1
    _mod = lambda: n if mod is None else n % mod 
    for bit in bin(exp)[2:]:
        n *= n 
        n = _mod()
        if bit == "1":
            n *= base
            n = _mod()
    return n

def powmod(base, exp, mod):
    n = 1
    for i in range(exp):
        n = (n * base) % mod
    return n

def timer(fn):
    start = time.perf_counter()
    value = fn()
    return value, time.perf_counter() - start

nums = (25234, 27192242, 856)
print("Builtin method:", timer(lambda: pow(*nums)))
print("Using iterative multiplication:", timer(lambda: powmod(*nums)))
print("Using square-multiply algorithm:", timer(lambda: square_mult(*nums)))
