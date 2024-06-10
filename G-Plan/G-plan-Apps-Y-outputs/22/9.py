
def find_potential_coordinates(K, X):
    potential_coords = []
    for i in range(X - K + 1, X + K + 1):
        potential_coords.append(i)
    return sorted(potential_coords)

if __name__ == "__main__":
    K, X = map(int, input().split())
    result = find_potential_coordinates(K, X)
    print(*result)
