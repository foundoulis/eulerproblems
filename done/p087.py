
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

total = 50000000
set_of_ints = set()
for square in gen_primes():
    for cube in gen_primes():
        for fourth in gen_primes():
            current = fourth**4 + cube**3 + square**2
            if current > total:
                break
            else:
                set_of_ints.add(current)
        if square**2 + cube**3 > total:
            break
    if square**2 > total:
        break
print(len(set_of_ints))
