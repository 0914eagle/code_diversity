
def get_similar_pairs(arr):
    n = len(arr)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] % 2 == arr[j] % 2 or abs(arr[i] - arr[j]) == 1:
                pairs.append([arr[i], arr[j]])
                break
    return pairs

def solve(arr):
    n = len(arr)
    pairs = get_similar_pairs(arr)
    if len(pairs) == n/2:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

