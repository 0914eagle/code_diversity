
def find_triangle(arr):
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            if arr[i] + arr[left] > arr[right]:
                return [i + 1, left + 1, right + 1]
            elif arr[i] + arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
    return [-1]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*find_triangle(arr))

if __name__ == '__main__':
    main()

