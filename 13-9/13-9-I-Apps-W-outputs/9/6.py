
def get_maximum_distance(n, x, a, b):
    if x == 0:
        return abs(a - b)
    
    # Initialize the maximum distance
    max_distance = 0
    
    # Iterate over all possible swaps
    for i in range(x):
        # Get the distance between the rivals before the swap
        before_swap = abs(a - b)
        
        # Swap the students
        a, b = b, a
        
        # Get the distance between the rivals after the swap
        after_swap = abs(a - b)
        
        # Update the maximum distance
        max_distance = max(max_distance, after_swap)
    
    return max_distance

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_maximum_distance(n, x, a, b))

if __name__ == '__main__':
    main()

