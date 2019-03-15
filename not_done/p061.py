
def general_polygonal_number(r, n):
    return (n*((n-1)*r - 2*(n-2)))//2

def split_number(n):
    return (n//100, n%100)

def gen_numbers(start=1, end=0):
    yield start
    i = start + 1
    while i != end:
        yield i 
        i += 1

def is_cyclic(numbs):
    # Given a set numbs, return if the set is cyclic
    pairs = []
    for elem in numbs:
        pairs.append(split_number(elem))
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            
            

th = 1000
tt = 10000
for t in gen_numbers():
    triangle = general_polygonal_number(3, t)
    if triangle < th:
        continue
    if triangle > tt:
        break
    if split_number(triangle)[1] < 10:
        continue
    for s in gen_numbers():
        square = general_polygonal_number(4, s)
        if square < th:
            continue
        if square > tt:
            break
        if split_number(square)[1] < 10:
            continue
        for p in gen_numbers():
            pentagon = general_polygonal_number(5, p)
            if pentagon < th:
                continue
            if pentagon > tt:
                break
            if split_number(pentagon)[1] < 10:
                continue
            for x in gen_numbers():
                hexagon = general_polygonal_number(6, x)
                if hexagon < th:
                    continue
                if hexagon > tt:
                    break
                if split_number(hexagon)[1] < 10:
                    continue
                for h in gen_numbers():
                    heptagon = general_polygonal_number(7, h)
                    if heptagon < th:
                        continue
                    if heptagon > tt:
                        break
                    if split_number(heptagon)[1] < 10:
                        continue
                    for o in gen_numbers():
                        octagon = general_polygonal_number(8, o)
                        if octagon < th:
                            continue
                        if octagon > tt:
                            break
                        if split_number(octagon)[1] < 10:
                            continue
                        test_set = [triangle, square, pentagon, hexagon, heptagon, octagon]
                        if len(test_set) != 6:
                            continue
                        print(is_cyclic(test_set))
