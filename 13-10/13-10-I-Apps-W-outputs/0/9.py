
def solve(arr):
    n = len(arr)
    if n == 1:
        return 1

    count = 0
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            count += 1

    return n - count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

if __name__ == '__main__':
    main()

