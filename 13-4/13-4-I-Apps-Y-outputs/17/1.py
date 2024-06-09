
import math

def solve(N, towns):
    paths = []
    for i in range(N):
        for j in range(i+1, N):
            paths.append(math.sqrt((towns[i][0]-towns[j][0])**2 + (towns[i][1]-towns[j][1])**2))
    return sum(paths) / len(paths)

if __name__ == "__main__":
    N = int(input())
    towns = []
    for i in range(N):
        towns.append(list(map(int, input().split())))
    print(solve(N, towns))

