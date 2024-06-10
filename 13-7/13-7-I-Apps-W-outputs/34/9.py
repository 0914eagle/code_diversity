
import sys

def get_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def is_perfect_matching(R, B, rebels, bases):
    visited = [False] * R
    for i in range(B):
        for j in range(R):
            if visited[j]:
                continue
            if rebels[j][0] == bases[i][0] and rebels[j][1] == bases[i][1]:
                visited[j] = True
                break
        else:
            return False
    return True

def solve():
    R, B, rebels, bases = get_input()
    if is_perfect_matching(R, B, rebels, bases):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()

