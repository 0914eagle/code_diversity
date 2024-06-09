
def find_path(n, p):
    path = [1]
    for i in range(2, n+1):
        if p[i-1] == 0:
            path.append(i)
        else:
            path.append(path[p[i-1]-1])
    return path

