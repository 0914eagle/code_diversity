
import sys

def solve():
    N, M = map(int, input().split())
    cities = []
    for _ in range(M):
        P, Y = map(int, input().split())
        cities.append((P, Y))

    cities.sort(key=lambda x: (x[0], x[1]))

    id_numbers = []
    for i in range(M):
        P, Y = cities[i]
        x = i + 1
        id_number = str(P).zfill(6) + str(x).zfill(6)
        id_numbers.append(id_number)

    return "\n".join(id_numbers)

if __name__ == "__main__":
    print(solve())

