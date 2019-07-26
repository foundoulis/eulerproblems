
import random

def is_sorted(l):
    if len(l) == 1: 
        return True
    elif l[0] <= l[1]:
        return True and is_sorted(l[1:])
    else:
        return False

def bozo_sort(l):
    trials = 0
    while True:
        if is_sorted(l):
            return trials

        how_many = random.randint(0, 3)
        if how_many == 0:
            continue
        trials += 1
        swap_rule = random.sample(range(0, len(l)), how_many)
        temp = l[swap_rule[0]]
        for index in range(len(swap_rule)-1):
            l[swap_rule[index]] = l[swap_rule[index+1]]
        l[swap_rule[-1]] = temp

        # print(l)
        
perm = list(range(4))
random.shuffle(perm)

summ = 0
for i in range(1000):
    random.shuffle(perm)
    summ += bozo_sort(perm)

print(summ/1000)

