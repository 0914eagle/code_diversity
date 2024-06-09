
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # initialize the maximum product
    max_product = 1
    
    # iterate over the array
    for i in range(n):
        # calculate the product of the elements from index 0 to i
        product = 1
        for j in range(i+1):
            product *= arr[j]
        
        # update the maximum product
        max_product = max(max_product, product)
    
    return max_product

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_product(arr))

if __name__ == '__main__':
    main()

