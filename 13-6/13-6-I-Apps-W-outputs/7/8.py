
def get_router_path(n, p):
    path = [1]
    for i in range(2, n+1):
        if i != p[i-1]:
            path.append(i)
    return path

