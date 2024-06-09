
import sys

def reconstruct_map(table):
    n = len(table)
    map = []
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != 0:
                map.append([i+1, j+1])
    return map

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append([int(x) for x in input().split()])
    map = reconstruct_map(table)
    for edge in map:
        print("{} {}".format(edge[0], edge[1]))

if __name__ == "__main__":
    main()

