
def solve(N, A, B):
    blue_balls = 0
    for i in range(N):
        if i % (A + B) < A:
            blue_balls += 1
    return blue_balls

