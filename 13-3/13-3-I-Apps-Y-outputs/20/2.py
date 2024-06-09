
def can_sort_array(arr, positions):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j] and j not in positions:
                return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        positions = set(map(int, input().split()))
        print(can_sort_array(arr, positions))

if __name__ == '__main__':
    main()

