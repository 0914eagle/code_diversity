
def get_impossible_triangle(arr):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[j] + arr[k] > arr[i]:
                    return [i + 1, j + 1, k + 1]
    return -1

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_impossible_triangle(arr))

if __name__ == '__main__':
    main()

