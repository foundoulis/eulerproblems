
M_map = {}
def M(n, c):
    if (n, c) == (3,1):
        return 4
    # elif (n, c) == (3,2):
    #     return 40
    elif (n, c) in M_map:
        return M_map[(n,c)]
    else:
        M_map[(n,c)] = n*M(n-1,c)
        return M_map[(n,c)]

print(4, M(3,1))
print(40, M(3,2))
