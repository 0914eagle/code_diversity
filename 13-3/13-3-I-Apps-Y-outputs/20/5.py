
import sys

def solve():
    N, M = map(int, input().split())
    cities = []
    for _ in range(M):
        P, Y = map(int, input().split())
        cities.append((P, Y))

    cities.sort(key=lambda x: (x[0], x[1]))

    id_numbers = []
    for i in range(N):
        prefecture = cities[i][0]
        x = 1
        while i < M and cities[i][0] == prefecture:
            id_number = str(prefecture).zfill(6) + str(x).zfill(6)
            id_numbers.append(id_number)
            i += 1
            x += 1

    return "\n".join(id_numbers)

if __name__ == "__main__":
    print(solve())

