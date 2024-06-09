
def get_median(arr):
    
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]

def count_pairs(arr, m):
    
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if get_median(arr[i:j+1]) == m:
                count += 1
    return count

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_pairs(arr, m))

if __name__ == '__main__':
    main()

