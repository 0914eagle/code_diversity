
def get_min_length(arr):
    n = len(arr)
    if n == 1:
        return 1
    
    # sort the array in descending order
    arr.sort(reverse=True)
    
    # initialize variables for the minimum length and the current length
    min_length = n
    current_length = n
    
    # loop through the array and find the minimum length
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            current_length -= 1
        else:
            min_length = min(min_length, current_length)
            current_length = n - i - 1
    
    # return the minimum length
    return min_length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_min_length(arr))

if __name__ == '__main__':
    main()

