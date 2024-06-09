
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
    
    # if all numbers are positive, return the array as is
    if neg_idx == n:
        return arr
    
    # find the index of the first positive number
    pos_idx = neg_idx
    while arr[pos_idx] > 0:
        pos_idx += 1
    
    # if there are no positive numbers, return the array with all negative numbers
    if pos_idx == n:
        return [-x for x in arr]
    
    # find the maximum product of positive numbers
    max_prod = 1
    for i in range(pos_idx, n):
        max_prod *= arr[i]
    
    # find the minimum product of negative numbers
    min_prod = 1
    for i in range(neg_idx):
        min_prod *= arr[i]
    
    # if the product of positive numbers is greater than the product of negative numbers, return the array as is
    if max_prod > abs(min_prod):
        return arr
    
    # otherwise, return the array with all negative numbers
    return [-x for x in arr]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = get_max_product(arr)
    print(*result)

if __name__ == '__main__':
    main()

