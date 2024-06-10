
def get_min_moves(a):
    n = len(a)
    left, right = 0, 0
    for i in range(n):
        if a[i] == 1:
            right = i
            break
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            left = i
            break
    return right - left + 1

def get_min_moves_recursive(a, left, right):
    n = len(a)
    if left == right:
        return 0
    if a[left] == 0 or a[right] == 0:
        return n
    if a[left] == 1 and a[right] == 1:
        return get_min_moves_recursive(a, left+1, right-1)
    if a[left] == 0 and a[right] == 1:
        return 1 + get_min_moves_recursive(a, left, right-1)
    if a[left] == 1 and a[right] == 0:
        return 1 + get_min_moves_recursive(a, left+1, right)

def get_min_moves_iterative(a):
    n = len(a)
    left, right = 0, 0
    for i in range(n):
        if a[i] == 1:
            right = i
            break
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            left = i
            break
    return right - left + 1

def get_min_moves_brute_force(a):
    n = len(a)
    min_moves = n
    for i in range(n):
        for j in range(i, n):
            if a[i] == 0 or a[j] == 0:
                continue
            movies = 0
            for k in range(i, j+1):
                if a[k] == 1:
                    movies += 1
            if movies < min_moves:
                min_moves = movies
    return min_moves

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_min_moves(a))
        print(get_min_moves_recursive(a, 0, n-1))
        print(get_min_moves_iterative(a))
        print(get_min_moves_brute_force(a))

