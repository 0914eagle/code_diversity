
def get_divisible_array(a, k):
    # Initialize variables
    x = 0
    n = len(a)
    moves = 0
    
    # Loop through the array
    for i in range(n):
        # If the current element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1
    
    # Return the minimum number of moves required to obtain a divisible array
    return moves

def get_divisible_array_2(a, k):
    # Initialize variables
    x = 0
    n = len(a)
    moves = 0
    
    # Loop through the array
    for i in range(n):
        # If the current element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1
    
    # Return the minimum number of moves required to obtain a divisible array
    return moves

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_divisible_array(a, k))

