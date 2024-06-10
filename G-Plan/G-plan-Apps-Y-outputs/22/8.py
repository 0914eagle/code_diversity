
def potential_black_stones(K, X):
    potential_coordinates = []
    for i in range(X - K + 1, X + K):
        potential_coordinates.append(i)
    potential_coordinates.sort()
    return potential_coordinates

if __name__ == "__main__":
    K, X = map(int, input().split())
    result = potential_black_stones(K, X)
    print(*result)
