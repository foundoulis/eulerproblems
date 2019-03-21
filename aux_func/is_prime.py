
from gen_primes import gen_primes

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