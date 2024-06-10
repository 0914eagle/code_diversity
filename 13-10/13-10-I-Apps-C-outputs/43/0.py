
import sys
import math

def get_input():
    n = int(input())
    people = []
    for i in range(n):
        a, b, c = map(int, input().split())
        people.append((a, b, c))
    return people

def get_weighted_order(people, S, T):
    order = []
    for a, b, c in people:
        order.append((a*S + b*T, a, b, c))
    return sorted(order)

def get_cluster_size(order):
    cluster_size = 0
    for i in range(len(order)):
        if order[i][3] == 1:
            cluster_size += 1
            j = i
            while j < len(order) and order[j][3] == 1:
                j += 1
            return cluster_size + len(order) - j
    return 0

def solve(people):
    min_cluster_size = math.inf
    for S in range(1000):
        for T in range(1000):
            order = get_weighted_order(people, S, T)
            cluster_size = get_cluster_size(order)
            if cluster_size < min_cluster_size:
                min_cluster_size = cluster_size
    return min_cluster_size

if __name__ == '__main__':
    people = get_input()
    print(solve(people))

