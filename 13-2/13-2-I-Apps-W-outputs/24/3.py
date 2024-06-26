
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # initialize the maximum product to be the product of the first two elements
    max_product = arr[0] * arr[1]
    
    # loop through the array and find the maximum product by multiplying the elements
    for i in range(2, n):
        max_product = max(max_product, arr[i-1] * arr[i])
    
    return max_product

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_product(arr))

if __name__ == '__main__':
    main()

