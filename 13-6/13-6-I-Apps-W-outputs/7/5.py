
def find_path(n, p):
    path = [1]
    for i in range(n-1):
        path.append(p[i])
    return path

