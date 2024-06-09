
def f1(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the minimum size of the subsegment to remove
    min_size = 0
    
    # Iterate through the array
    for i in range(n - 1):
        # If the current element is equal to the next element, increment the minimum size
        if arr[i] == arr[i + 1]:
            min_size += 1
    
    return min_size

def f2(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the minimum size of the subsegment to remove
    min_size = 0
    
    # Iterate through the array
    for i in range(n - 1):
        # If the current element is equal to the next element, increment the minimum size
        if arr[i] == arr[i + 1]:
            min_size += 1
    
    return min_size

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(f1(n, arr))
    print(f2(n, arr))

