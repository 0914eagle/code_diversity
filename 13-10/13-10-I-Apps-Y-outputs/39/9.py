
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def find_similar_pairs(arr):
    n = len(arr)
    if n % 2 == 1:
        return "NO"
    for i in range(0, n, 2):
        x = arr[i]
        y = arr[i + 1]
        if not is_similar(x, y):
            return "NO"
    return "YES"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_similar_pairs(arr))

