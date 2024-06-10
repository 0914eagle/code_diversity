
def solve(arr):
    n = len(arr)
    if n == 1:
        return 1
    
    # find the first pair of equal elements
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            break
    
    # if no pair of equal elements found, return the length of the array
    if i == n-1:
        return n
    
    # replace the pair of equal elements by one element with value arr[i] + 1
    arr[i] += 1
    
    # recursively solve the problem for the remaining elements
    return 1 + solve(arr[i+1:])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

if __name__ == '__main__':
    main()

