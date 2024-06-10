
def input_data():
    N = int(input())
    arr = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    return N, arr, Q, queries

def is_magical(arr):
    return all(arr[0] <= x <= arr[-1] for x in arr)

def get_longest_magical_subarray(arr, L, R):
    max_len = 0
    for i in range(L, R+1):
        for j in range(i, R+1):
            if is_magical(arr[i:j+1]):
                max_len = max(max_len, j-i+1)
    return max_len

def solve(N, arr, Q, queries):
    result = []
    for L, R in queries:
        result.append(get_longest_magical_subarray(arr, L, R))
    return result

if __name__ == '__main__':
    N, arr, Q, queries = input_data()
    result = solve(N, arr, Q, queries)
    for x in result:
        print(x)

