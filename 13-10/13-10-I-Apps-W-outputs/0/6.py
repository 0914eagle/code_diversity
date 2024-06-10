
def find_min_length(arr):
    n = len(arr)
    if n == 1:
        return 1
    
    # sort the array in descending order
    arr.sort(reverse=True)
    
    # initialize variables
    i = 0
    j = 1
    count = 0
    
    # loop through the array
    while i < n:
        if arr[i] == arr[j]:
            # if the current element is equal to the next element,
            # replace them by one element with value arr[i] + 1
            arr[i] += 1
            count += 1
            j += 1
        else:
            # if the current element is not equal to the next element,
            # move on to the next element
            i += 1
            j += 1
    
    # return the minimum length of the array
    return n - count

def main():
    arr = list(map(int, input().split()))
    print(find_min_length(arr))

if __name__ == '__main__':
    main()

