
def find_min_square_frame(screen):
    n, m = len(screen), len(screen[0])
    for i in range(n):
        for j in range(m):
            if screen[i][j] == "w":
                for k in range(i, n):
                    for l in range(j, m):
                        if screen[k][l] == "w":
                            return screen
    return "-1"

