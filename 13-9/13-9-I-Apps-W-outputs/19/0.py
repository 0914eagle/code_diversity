
def can_divide_array(arr):
    n = len(arr)
    sum1 = sum(arr[:n//2])
    sum2 = sum(arr[n//2:])
    if sum1 == sum2:
        return "YES"
    
    for i in range(n//2):
        if arr[i] + arr[n-1] == sum1:
            return "YES"
    
    return "NO"

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_divide_array(arr))

if __name__ == '__main__':
    main()

