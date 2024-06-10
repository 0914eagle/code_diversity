
def get_unique_element(arr):
    n = len(arr)
    if n == 1:
        return True
    if n == 2:
        return arr[0] == arr[1]
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) <= 1:
                return get_unique_element(arr[:i] + arr[i+1:] + arr[j+1:])
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES" if get_unique_element(arr) else "NO")

if __name__ == '__main__':
    main()

