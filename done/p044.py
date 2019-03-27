import math
from itertools import count


def general_polygonal_number(r, n):
    return (n*((n-1)*r - 2*(n-2)))//2


def pent_num(n):
    return general_polygonal_number(5, n)


def is_pent(inverted_n):  # Works up to 10**7 at least
    n = (1 + math.sqrt(24*inverted_n + 1))/6
    return((n - int(n)) == 0)


for y in count(1):
    for x in range(1, y):
        pn1 = pent_num(y)
        pn2 = pent_num(x)
        if is_pent(abs(pn1 - pn2)) and is_pent(pn1+pn2):
            print(pn1, pn2, pn1+pn2, pn1-pn2)
            exit(0)
