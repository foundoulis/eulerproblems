
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

summ = 0
for i in range(2,101):
    summ += P(i, 100)
print(summ)

