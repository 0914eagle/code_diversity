
def get_smallest_chessboard(n):
    for m in range(1, n):
        if is_valid_chessboard(m, n):
            return m
    return n

def is_valid_chessboard(m, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not is_valid_position(m, n, i, j):
                return False
    return True

def is_valid_position(m, n, i, j):
    for k in range(1, n+1):
        if k != i and k != j and is_neighbor(m, n, i, j, k):
            return False
    return True

def is_neighbor(m, n, i, j, k):
    if abs(i - k) + abs(j - k) < abs(i - j):
        return True
    return False

def get_position(m, n):
    positions = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if is_valid_position(m, n, i, j):
                positions.append((i, j))
    return positions

def main():
    n = int(input())
    m = get_smallest_chessboard(n)
    print(m)
    positions = get_position(m, n)
    for i in range(n):
        print(positions[i][0], positions[i][1])

if __name__ == '__main__':
    main()

