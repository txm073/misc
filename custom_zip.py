
def _zip(*iterables):
    return [tuple([iterable[j] for iterable in iterables]) 
            for j in range(min([len(i) for i in iterables]))]

for num in _zip([1, 2, 3, 4]):
    print(num)