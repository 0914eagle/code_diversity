
def get_min_d(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference between elements as the difference between the first two elements
    min_d = arr[1] - arr[0]
    
    # Iterate over the array and calculate the difference between each element and the previous element
    for i in range(1, len(arr)):
        d = arr[i] - arr[i-1]
        if d < min_d:
            min_d = d
    
    return min_d

def make_equal(arr):
    # Get the minimum difference between elements
    min_d = get_min_d(arr)
    
    # If the minimum difference is 0, all elements are already equal
    if min_d == 0:
        return arr
    
    # Otherwise, add the minimum difference to the first element and subtract it from the last element
    arr[0] += min_d
    arr[-1] -= min_d
    
    # Return the modified array
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(make_equal(arr))

if __name__ == '__main__':
    main()

