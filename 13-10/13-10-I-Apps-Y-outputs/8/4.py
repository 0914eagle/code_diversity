
def read_input():
    n = int(input())
    distances = []
    for i in range(n):
        distances.append(list(map(int, input().split())))
    return n, distances

def reconstruct_map(distances):
    n = len(distances)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if distances[i][j] != 0:
                roads.append((i+1, j+1))
    return roads

def write_output(roads):
    print(len(roads))
    for road in roads:
        print(' '.join(map(str, road)))

def main():
    n, distances = read_input()
    roads = reconstruct_map(distances)
    write_output(roads)

if __name__ == '__main__':
    main()

