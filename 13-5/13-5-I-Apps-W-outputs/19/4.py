
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # find the index of the first negative number
    neg_idx = 0
    while arr[neg_idx] < 0:
        neg_idx += 1
    
    # find the index of the first positive number
    pos_idx = neg_idx + 1
    while arr[pos_idx] > 0:
        pos_idx += 1
    
    # find the maximum product of the first negative number and the first positive number
    max_product = arr[neg_idx] * arr[pos_idx]
    
    # find the maximum product of the first negative number and the first positive number, after swapping them
    max_product_swap = arr[neg_idx] * arr[pos_idx] * arr[neg_idx + 1]
    
    # if the maximum product after swapping is greater than the current maximum product, then swap them
    if max_product_swap > max_product:
        arr[neg_idx], arr[pos_idx] = arr[pos_idx], arr[neg_idx]
        max_product = max_product_swap
    
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = get_max_product(arr)
    print(*result)

if __name__ == '__main__':
    main()

