
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # initialize the maximum product to be the product of all elements
    max_product = 1
    for i in range(n):
        max_product *= arr[i]
    
    # loop through each element and check if it can be made negative
    for i in range(n):
        if arr[i] > 0:
            continue
        # if the element is negative, make it positive and multiply it with -1
        arr[i] = -arr[i]
        max_product *= -1
    
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*get_max_product(arr))

