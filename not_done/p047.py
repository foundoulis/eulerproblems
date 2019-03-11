
# Too slow

def gen_primes():
    primes = [2]
    yield 2
    i = 3
    while True:
        is_prime = True
        for p in primes: 
            if i % p == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
            yield i
        i += 1

amor = {}
def factor(n):
    original_n = n
    if n in amor:
        return amor[n]
    else:     
        factors = {}
        while n != 1:
            for i in gen_primes():
                if n % i == 0: # i divides n evenly
                    if i in factors:
                        factors[i] += 1
                    else:
                        factors[i] = 1
                    n //= i # Remove the factor from n
                if i > n:
                    break
        amor[original_n] = len(list(factors.keys()))
        return amor[original_n]


k = 4
amorization = {}
def find_distincts(i):
    lists_of_factors = []
    for n in range(k):
        if (n+i) in amorization:
            lists_of_factors.append(amorization[n+i])
        else: 
            amorization[n+i] = factor(i+n)
            lists_of_factors.append(amorization[n+i])
    same_length = True
    for lengths in lists_of_factors:
        if lengths != k:
            same_length = False
    return (i, same_length)

i = 2
while True:
    result = find_distincts(i)
    if result[1]:
        print(f"Found {result[0]}")
        break
    if i % 100 == 0:
        print(f"Looking at {i}-{i+99}")
    i += 1
            