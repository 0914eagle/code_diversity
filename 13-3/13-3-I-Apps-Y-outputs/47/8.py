
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_arr = sum(arr)
    min_sum = sum_arr
    parity = 0
    deleted_elements = []
    
    # Iterate through the array
    for i in range(n):
        # If it's the first move, choose any element and delete it
        if i == 0:
            deleted_elements.append(arr[i])
            parity = arr[i] % 2
            continue
        
        # If it's the second or any next move, choose an element with the only restriction: its parity should differ from the parity of the element deleted on the previous move
        if parity == 0:
            # If the last deleted element was odd, choose any even element and delete it
            if arr[i] % 2 == 0:
                deleted_elements.append(arr[i])
                parity = 1
        else:
            # If the last deleted element was even, choose any odd element and delete it
            if arr[i] % 2 == 1:
                deleted_elements.append(arr[i])
                parity = 0
    
    # If after some move Polycarp cannot make a move, the game ends
    if len(deleted_elements) == n:
        return sum_arr
    
    # If Polycarp can delete the whole array, then the sum of non-deleted elements is zero
    return 0

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_min_sum(arr))

