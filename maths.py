import math 
from decimal import Decimal, getcontext
from time import perf_counter

ITERATIONS = 10000000

def timed(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = fn(*args, **kwargs)
        return value, perf_counter() - start
    return wrapper

def fact(n):
    output = 1
    for i in range(1, int(n) + 1):
        output *= i
    return output

def calc_e():
    output = 0
    for i in range(18):
        output += (1 / fact(i))
    return output

@timed
def chudnovsky(digits):
    output = Decimal(0)
    for i in range(digits):
        numerator = ((-1) ** i) * (fact(6 * i)) * (545140134 * i + 13591409)  
        denominator = fact(2 * i) * (fact(i) ** 3) * 640320 ** (3 * i + 1.5)
        output += (Decimal(numerator) / Decimal(denominator))
    return round(1 / (12 * output), digits)


pi = chudnovsky(15)[0]
print(pi)
print(len(str(pi)))