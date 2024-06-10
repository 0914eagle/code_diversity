
import sys

def get_input():
    n = int(input())
    people = []
    for i in range(n):
        a, b, c = map(int, input().split())
        people.append((a, b, c))
    return n, people

def find_optimal_weight(n, people):
    optimal_cluster_size = sys.maxsize
    for S in range(-100, 101):
        for T in range(-100, 101):
            cluster_size = 0
            for i in range(n):
                if people[i][2] == 1:
                    cluster_size += 1
            if cluster_size < optimal_cluster_size:
                optimal_cluster_size = cluster_size
    return optimal_cluster_size

def main():
    n, people = get_input()
    print(find_optimal_weight(n, people))

if __name__ == '__main__':
    main()

