
import itertools

value_storage = {}
def P(k, n):
    if (k, n) in value_storage:
        return value_storage[(k, n)]
    if k == 1:
        return 1
    if k > n:
        return 0
    if n == 0:
        return 
    value_storage[(k, n)] = P(k, n-k) + P(k-1, n-1)
    return value_storage[(k, n)]

def p(n):
    summ = 0
    for i in range(1,n+1):
        summ += P(i, n)
    return summ

for i in itertools.count(1):
# for i in range(1, 11):
    value = p(i)
    print(f"p({i}) = {value}")
    # if i % 1000 == 0:
    if value % 1000000 == 0:
        print(f"Done. Value is {i}")
        break

