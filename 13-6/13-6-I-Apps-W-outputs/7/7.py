
def find_path(n, p):
    path = [1]
    for i in range(n-1):
        next_router = p[i]
        while next_router in path:
            next_router += 1
        path.append(next_router)
    return path

