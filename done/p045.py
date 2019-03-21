def general_polygonal_number(r, n):
    return (n*((n-1)*r - 2*(n-2)))//2

max_i = 100000

tris = set(general_polygonal_number(3, x) for x in range(max_i))
pents = set(general_polygonal_number(5, x) for x in range(max_i))
hexs = set(general_polygonal_number(6, x) for x in range(max_i))

# print(tris)

print(tris.intersection(pents, hexs))
