
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

prime_yes_no = {}
def is_prime(n):
    if n in prime_yes_no:
        return prime_yes_no[n]
    if n == 1:
        return False
    for p in gen_primes():
        if p*p > n:
            break
        if n % p == 0:
            prime_yes_no[n] = False
            return False
    prime_yes_no[n] = True
    return True

def truncate_left(n):
    return n%10**int(math.log10(n))

def truncate_right(n):
    return n//10

def truncate_list(n):
    extra_n = n
    left_list = []
    while n >= 1:
        left_list.append(n)
        n = truncate_left(n)
    right_list = []
    while extra_n >= 1:
        right_list.append(extra_n)
        extra_n = truncate_right(extra_n)
    return [left_list, right_list]

trunc_primes = []
for p in gen_primes():
    if p < 10:
        continue
    trunc_prime = True
    nums = truncate_list(p)
    for i in nums[0]:
        if not is_prime(i):
            trunc_prime = False
            break
    if trunc_prime:
        for i in nums[1]:
            if not is_prime(i):
                trunc_prime = False
                break
    if trunc_prime:
        print(p)
        trunc_primes.append(p)
        print(trunc_primes)
    if len(trunc_primes) == 11:
        print(trunc_primes)
        print(sum(trunc_primes))

