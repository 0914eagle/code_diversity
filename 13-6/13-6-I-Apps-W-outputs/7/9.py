
def get_path(n, p):
    path = [1]
    for i in range(2, n+1):
        if p[i-1] != path[-1]:
            path.append(p[i-1])
    return path

