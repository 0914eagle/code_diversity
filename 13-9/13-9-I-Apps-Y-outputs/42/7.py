
def get_equal_elements(a, k):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of equal elements to 0
    equal_elements = 0
    # Loop through the array
    for i in range(len(a)):
        # If the current element is equal to the previous element
        if i > 0 and a[i] == a[i-1]:
            # Increment the number of equal elements
            equal_elements += 1
        # If the number of equal elements is greater than or equal to k
        if equal_elements >= k:
            # Return the number of moves
            return moves
        # If the current element is not equal to the previous element
        else:
            # Increment the number of moves
            moves += 1
            # Set the current element to the previous element
            a[i] = a[i-1]
    # If the number of equal elements is not greater than or equal to k
    return -1

def solve(n, k, a):
    # Get the equal elements in the array
    equal_elements = get_equal_elements(a, k)
    # If the number of equal elements is greater than or equal to k
    if equal_elements >= k:
        # Return the number of moves
        return equal_elements
    # If the number of equal elements is not greater than or equal to k
    else:
        # Return -1
        return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

