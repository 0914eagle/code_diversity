
def potential_black_stones(K, X):
    potential_coords = []
    for i in range(X - K + 1, X + K):
        potential_coords.append(i)
    return sorted(potential_coords)

if __name__ == "__main__":
    K, X = map(int, input().split())
    result = potential_black_stones(K, X)
    print(*result)
