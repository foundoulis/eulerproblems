
def general_polygonal_number(r, n):
    return (n*((n-1)*r - 2*(n-2)))//2

def split_number(n):
    return (n//100, n%100)

def is_cyclic(numbs):
    # Given a set numbs, return if the set is cyclic
    pairs = []
    for elem in numbs:
        pairs.append(split_number(elem))
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            pass
