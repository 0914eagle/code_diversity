
def find_min_size_frame(screen):
    n, m = len(screen), len(screen[0])
    for d in range(1, int(n/2)+1):
        for i in range(n-d):
            for j in range(m-d):
                if all(screen[i+k][j+k] == "w" for k in range(d)):
                    return d
    return -1

