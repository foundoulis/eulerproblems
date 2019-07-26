
def split(n): # log n time
    while n >= 1:
        yield n%10
        n //= 10

fancy_split_map = {}
def fancy_split(n):
    if n in fancy_split_map:
        return fancy_split_map[n]
    elif n//10 in fancy_split_map:
        fancy_split_map[n] = [n%10] + fancy_split_map[n//10]
        return fancy_split_map[n]
    elif len(list(split(n))) == 1:
        fancy_split_map[n] = [n]
        return [n]
    else:
        fancy_split_map[n] = [n%10] + fancy_split(n//10)
        return fancy_split_map[n]

def unsplit(digits): # log n time
    summ = 0
    for index, d in enumerate(digits):
        summ += d*10**(len(digits) - index - 1)
    return summ

def digits_are_odd(n): # log n time
    for d in fancy_split(n):
        if d%2 == 0:
            return False
    return True

not_reverseable = set()
reverseables = set()
for i in range(1,10**9):
    if i%10**6 == 0:
        print(i//10**6)
    if (i%10 != 0) and (i not in reverseables) and (i not in not_reverseable):
        digits_i = fancy_split(i)
        other_i = unsplit(digits_i)
        if digits_are_odd(i+other_i):
            reverseables.add(i)
            reverseables.add(other_i)
        else: 
            not_reverseable.add(i)
            not_reverseable.add(other_i)

r = list(reverseables)
r.sort()
print(r)
print(len(reverseables))

