
digits = []
starting = 2**1000
print(starting)
while starting > 0:
    digits.append(starting%10)
    starting = starting//10
print(digits)
print(sum(digits))
