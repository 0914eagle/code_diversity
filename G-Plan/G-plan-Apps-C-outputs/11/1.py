
def update_stones(arr, L, R, A, B):
    for i in range(L, R+1):
        arr[i-1] = (i - L + 1) * A % B

def total_stones(arr, L, R):
    return sum(arr[L-1:R])

if __name__ == '__main__':
    N, Q = map(int, input().split())
    stones = [0] * N

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            update_stones(stones, query[1], query[2], query[3], query[4])
        else:
            print(total_stones(stones, query[1], query[2]))
