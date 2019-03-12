
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


