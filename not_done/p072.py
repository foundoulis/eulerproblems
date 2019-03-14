from fractions import Fraction

# too slow

primes = {2: 3, 3: 5}
def gen_primes():
    i = 2
    yield i
    while True:
        if i in primes:
            yield primes[i]
            i = primes[i]
            continue
        is_prime = True
        for k,v in primes.items():
            if i % k == 0:
                is_prime = False
        if is_prime:
            previous_prime = 0
            for v in primes.values():
                if v > previous_prime:
                    previous_prime = v
            primes[previous_prime] = i
            yield primes[previous_prime]
        i += 1

amor = {}
def factor(n):
    if n == 1:
        return {1: 1}
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
        amor[original_n] = factors
        return amor[original_n]

def find_fraction_group_order(group):
    counting_set = set()
    for d in range(1,group+1):
        for n in range(1,d):
            counting_set.add(Fraction(n,d))
    return len(counting_set)

for i in range(1,5):
    thingy = find_fraction_group_order(10**i)
    print(f"{10**i} gives {thingy} = {factor(thingy)}")
