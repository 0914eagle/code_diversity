
def solve(a, k):
    # Step 1: Find the minimum and maximum values in the array
    min_val = min(a)
    max_val = max(a)
    
    # Step 2: Initialize the number of moves to 0
    moves = 0
    
    # Step 3: Loop until we have at least k equal elements in the array
    while True:
        # Step 3.1: If the minimum value is equal to the maximum value, we are done
        if min_val == max_val:
            break
        
        # Step 3.2: If the minimum value is less than the maximum value, we need to increase the minimum value
        if min_val < max_val:
            # Find the index of the minimum value and increase it by 1
            min_index = a.index(min_val)
            a[min_index] += 1
            moves += 1
            
            # Update the minimum and maximum values
            min_val = min(a)
            max_val = max(a)
            
        # Step 3.3: If the minimum value is greater than the maximum value, we need to decrease the maximum value
        else:
            # Find the index of the maximum value and decrease it by 1
            max_index = a.index(max_val)
            a[max_index] -= 1
            moves += 1
            
            # Update the minimum and maximum values
            min_val = min(a)
            max_val = max(a)
    
    return moves

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, k))

if __name__ == '__main__':
    main()

