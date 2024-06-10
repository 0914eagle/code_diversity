
def is_magical(arr):
    return all(arr[0] <= x <= arr[-1] for x in arr)

def get_longest_magical_subarray(arr, l, r):
    longest = 0
    for i in range(l, r+1):
        subarr = arr[i:r+1]
        if is_magical(subarr) and len(subarr) > longest:
            longest = len(subarr)
    return longest

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(get_longest_magical_subarray(arr, l, r))

if __name__ == '__main__':
    main()

