
def get_magical_subarray(arr, l, r):
    max_length = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if is_magical(arr[i:j+1]):
                max_length = max(max_length, j-i+1)
    return max_length

def is_magical(arr):
    return all(arr[0] <= x <= arr[-1] for x in arr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(get_magical_subarray(arr, l, r))

if __name__ == '__main__':
    main()

