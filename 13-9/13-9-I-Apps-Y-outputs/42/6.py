
def get_min_moves(a, k):
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the number of moves to 0
    moves = 0
    
    # Initialize the number of equal elements to 0
    equal_elements = 0
    
    # Iterate through the array
    for i in range(len(a)):
        # If the current element is equal to the previous element, increment the number of equal elements
        if i > 0 and a[i] == a[i-1]:
            equal_elements += 1
        # If the current element is not equal to the previous element and the number of equal elements is less than k, make a move
        elif equal_elements < k:
            # If the current element is the minimum element, increase its value by one and make a move
            if a[i] == min(a):
                a[i] += 1
                moves += 1
            # If the current element is the maximum element, decrease its value by one and make a move
            elif a[i] == max(a):
                a[i] -= 1
                moves += 1
        
        # If the number of equal elements is greater than or equal to k, break the loop
        if equal_elements >= k:
            break
    
    # Return the minimum number of moves required to obtain at least k equal elements in the array
    return moves

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_min_moves(a, k))

if __name__ == '__main__':
    main()

