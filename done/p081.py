
content = None
with open("p081_matrix.txt") as f:
    content = f.readlines()

content = [x.strip().split(",") for x in content]
content = [[int(y) for y in x] for x in content]

amorization = {}
def min_path(x,y):
    if (x,y) in amorization:
        return amorization[(x,y)]
    elif x == 0 and y == 0:
        return content[0][0]
    elif x == 0:
        amorization[(x,y)] = min_path(x, y-1) + content[x][y]
        return amorization[(x,y)]
    elif y == 0:
        amorization[(x,y)] = min_path(x-1, y) + content[x][y]
        return amorization[(x,y)]
    else:
        amorization[(x,y)] = min(min_path(x-1, y), min_path(x, y-1)) + content[x][y]
        return amorization[(x,y)]

print(min_path(79,79))