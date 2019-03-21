import math

def general_polygonal_number(r, n):
    return (n*((n-1)*r - 2*(n-2)))//2

def pent_num(n):
    return general_polygonal_number(5, n)

def is_pentagonal(k):
    return (1/6)*(math.sqrt(24*k + 1) + 1)

max_i = 1000
pent_nums = set()
for j in range(max_i):
    pent_nums.add(pent_num(j))
    for k in range(j):
        if k is pentagonal: # do stuff
    
