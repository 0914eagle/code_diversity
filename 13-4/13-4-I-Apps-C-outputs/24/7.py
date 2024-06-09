
def f1(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time to reach a1 and a2
    min_time = 0
    # Initialize the current heights of Xaniar and Abol
    current_h1 = h1
    current_h2 = h2
    # Loop until the heights of Xaniar and Abol are equal to a1 and a2 respectively
    while current_h1 != a1 or current_h2 != a2:
        # Calculate the new heights of Xaniar and Abol after one second
        new_h1 = (x1 * current_h1 + y1) % m
        new_h2 = (x2 * current_h2 + y2) % m
        # Update the current heights of Xaniar and Abol
        current_h1 = new_h1
        current_h2 = new_h2
        # Increment the minimum time
        min_time += 1
    # Return the minimum time
    return min_time

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    m = int(input())
    h1 = int(input())
    a1 = int(input())
    x1 = int(input())
    y1 = int(input())
    h2 = int(input())
    a2 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(f1(m, h1, a1, x1, y1, h2, a2, x2, y2))

