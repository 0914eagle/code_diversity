
def get_median(arr):
    
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]

def get_pairs_with_median(arr, m):
    
    n = len(arr)
    count = 0
    for l in range(n):
        for r in range(l, n):
            if get_median(arr[l:r+1]) == m:
                count += 1
    return count

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_pairs_with_median(arr, m))

if __name__ == '__main__':
    main()

