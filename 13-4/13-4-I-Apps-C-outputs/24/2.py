
def f1(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time and the current heights
    min_time = 0
    curr_h1 = h1
    curr_h2 = h2
    
    # Loop until the heights of Xaniar and Abol are equal to a1 and a2 respectively
    while curr_h1 != a1 or curr_h2 != a2:
        # Calculate the new heights of Xaniar and Abol
        new_h1 = (x1 * curr_h1 + y1) % m
        new_h2 = (x2 * curr_h2 + y2) % m
        
        # Update the current heights
        curr_h1 = new_h1
        curr_h2 = new_h2
        
        # Increment the minimum time
        min_time += 1
    
    # Return the minimum time
    return min_time

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    m = int(input())
    h1, a1 = map(int, input().split())
    x1, y1 = map(int, input().split())
    h2, a2 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    print(f1(m, h1, a1, x1, y1, h2, a2, x2, y2))

