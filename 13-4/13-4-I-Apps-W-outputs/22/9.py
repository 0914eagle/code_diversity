
def f1(n, arr):
    # f1 function to reverse the array
    return arr[::-1]

def f2(n, arr):
    # f2 function to find the original order of the array
    
    # initialize an empty array to store the original order
    original_order = []
    
    # loop through the array
    for i in range(n):
        
        # find the index of the current element in the original array
        index = arr.index(i + 1)
        
        # add the element to the original order array
        original_order.append(arr[index])
    
    # return the original order array
    return original_order

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*f2(n, f1(n, arr)))

