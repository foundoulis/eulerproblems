
number_to_factors = {}
def factors(n):
    if n in number_to_factors:
        return number_to_factors[n]
    else: 
        number_to_factors[n] = sum(filter(lambda x: n%x==0, (x for x in range(1,n))))
        return number_to_factors[n]


a_numbers = set()
for x in range(1,10000):
    for y in range(x+1,10000):
        if factors(x) == y and factors(y) == x:
            a_numbers.add(x)
            a_numbers.add(y)
print(a_numbers)
print(sum(a_numbers))
