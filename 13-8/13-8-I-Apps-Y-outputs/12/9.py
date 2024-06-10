
def get_minimum_moves(a, k):
    # Initialize variables
    x = 0
    moves = 0
    n = len(a)
    
    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1
    
    # Return the minimum number of moves required to make all elements divisible by k
    return moves

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Call the get_minimum_moves function and print the result
        print(get_minimum_moves(a, k))

if __name__ == '__main__':
    main()

