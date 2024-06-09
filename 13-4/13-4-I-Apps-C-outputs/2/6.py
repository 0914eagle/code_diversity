
def f1(n, r, w, h):
    # Initialize the maximum number of gems that can be collected
    max_gems = 0
    
    # Iterate through the gems
    for i in range(n):
        # Read the next gem's coordinates
        x, y = map(int, input().split())
        
        # Calculate the distance from the current position to the gem
        distance = abs(x - w) + abs(y - h)
        
        # Calculate the time it takes to reach the gem
        time = distance / r
        
        # Update the maximum number of gems that can be collected
        max_gems = max(max_gems, i + 1)
    
    return max_gems

def f2(...):
    ...

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))

