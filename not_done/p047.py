from itertools import count

primes = set()
composites = set()
def is_prime(n):
    if n in primes:
        return True
    if n in composites:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for i in count(2):
        if n % i == 0:
            composites.add(n)
            return False
        if i*i > n:
            break
    primes.add(n)
    return True

for i in range(100):
    if is_prime(i):
        print(i)

            