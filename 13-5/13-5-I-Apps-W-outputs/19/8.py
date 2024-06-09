
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # initialize the maximum product
    max_product = 1
    
    # loop through the array and calculate the product
    # of all positive numbers
    product = 1
    for i in range(n):
        if arr[i] > 0:
            product *= arr[i]
            max_product = max(max_product, product)
        else:
            product *= -1
    
    # return the array with the maximum product
    return [int(x) for x in str(max_product)]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = get_max_product(arr)
    print(*result)

if __name__ == '__main__':
    main()

