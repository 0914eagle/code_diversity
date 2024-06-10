
import sys
import itertools

def get_input():
    n, k, a, b = map(int, input().split())
    tastiness = list(map(int, input().split()))
    complement_matrix = []
    for i in range(k):
        complement_matrix.append(list(map(int, input().split())))
    return n, k, a, b, tastiness, complement_matrix

def calculate_tastiness(tastiness, complement_matrix, n):
    total_tastiness = 0
    for combination in itertools.combinations(range(k), n):
        current_tastiness = 0
        for i in range(n):
            current_tastiness += tastiness[combination[i]]
            for j in range(i+1, n):
                current_tastiness += complement_matrix[combination[i]][combination[j]]
        total_tastiness = max(total_tastiness, current_tastiness)
    return total_tastiness

def calculate_cost(n, a, b):
    return n * a + b

def get_ratio(tastiness, complement_matrix, n, a, b):
    total_tastiness = calculate_tastiness(tastiness, complement_matrix, n)
    total_cost = calculate_cost(n, a, b)
    if total_cost == 0:
        return 0
    return total_tastiness / total_cost

def main():
    n, k, a, b, tastiness, complement_matrix = get_input()
    ratio = get_ratio(tastiness, complement_matrix, n, a, b)
    print(ratio)

if __name__ == '__main__':
    main()

