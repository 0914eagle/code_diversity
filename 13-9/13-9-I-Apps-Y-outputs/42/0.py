
def get_min_moves(a, k):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of equal elements to 0
    equal_elements = 0
    # Loop through the array
    for i in range(len(a)):
        # If the current element is equal to the previous element, increment the number of equal elements
        if i > 0 and a[i] == a[i-1]:
            equal_elements += 1
        # If the number of equal elements is greater than or equal to k, return the number of moves
        if equal_elements >= k:
            return moves
        # If the current element is not equal to the previous element, reset the number of equal elements to 1
        else:
            equal_elements = 1
        # Increment the number of moves
        moves += 1
    # If all elements are unique, return -1
    return -1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_min_moves(a, k))

if __name__ == '__main__':
    main()

