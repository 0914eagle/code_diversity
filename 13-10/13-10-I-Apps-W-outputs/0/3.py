
def find_min_length(arr):
    n = len(arr)
    if n == 1:
        return 1
    
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize the minimum length as the length of the array
    min_length = n
    
    # Iterate over the array and find the minimum length
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            min_length = min(min_length, i+1)
    
    return min_length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_min_length(arr))

if __name__ == '__main__':
    main()

