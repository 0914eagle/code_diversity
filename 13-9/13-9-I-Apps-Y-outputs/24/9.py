
def get_max_diff(arr):
    n = len(arr)
    max_diff = 0
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_diff(arr))

if __name__ == '__main__':
    main()

