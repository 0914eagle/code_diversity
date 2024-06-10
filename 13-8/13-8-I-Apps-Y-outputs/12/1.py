
def get_divisible_array(a, k):
    # Initialize variables
    x = 0
    n = len(a)
    moves = 0
    
    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1
    
    # Return the minimum number of moves required to make the array divisible by k
    return moves

def get_minimum_moves(a, k):
    # Initialize variables
    n = len(a)
    moves = [0] * n
    
    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            moves[i] = 1
    
    # Return the minimum number of moves required to make the array divisible by k
    return sum(moves)

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_divisible_array(a, k))
        print(get_minimum_moves(a, k))

if __name__ == '__main__':
    main()

