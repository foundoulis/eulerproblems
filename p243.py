from fractions import Fraction

primes = [2]
def gen_primes():
    yield 2
    curr_prod = 2
    i = 3
    while True:
        is_prime = True
        for p in primes: 
            if i % p == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
            curr_prod *= i
            yield curr_prod
        i += 1

amor = {}
def greatest(a, b): 
    if (a, b) in amor: 
        return amor[(a,b)]
    if b == 0:
        amor[(a,b)] = a
        return amor[(a,b)]
    return greatest(b, a % b)

def is_resilient(num, den):
    if greatest(num, den) == 1:
        return True
    return False

def R(d):
    total = 0
    for i in range(1, d):
        if is_resilient(i, d):
            total += 1
    return Fraction(total, d-1)

f = Fraction(15499, 94744)
print(f"trying to get to: {float(f)}")
current_lowest = Fraction(1,1)

i = 223092870
while True:
    r = R(i)
    if r < current_lowest:
        print(f"Current lowest is {i}, with {float(r)}")
        current_lowest = r
    if r < f:
        print(f"Found {i}")
        break
    i += 223092870
