
def get_black_coordinates(K, X):
    
    black_coordinates = []
    for i in range(X - K + 1, X + 1):
        black_coordinates.append(i)
    for i in range(X + 1, X + K + 1):
        if i <= 1000000:
            black_coordinates.append(i)
    return black_coordinates

def main():
    K, X = map(int, input().split())
    black_coordinates = get_black_coordinates(K, X)
    print(*black_coordinates)

if __name__ == '__main__':
    main()

