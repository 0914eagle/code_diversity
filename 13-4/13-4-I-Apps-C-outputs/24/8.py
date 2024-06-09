
def f1(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0
    # Initialize the current heights of Xaniar and Abol as h1 and h2 respectively
    curr_h1, curr_h2 = h1, h2
    # Loop until the heights of Xaniar and Abol are equal to a1 and a2 respectively
    while curr_h1 != a1 or curr_h2 != a2:
        # Calculate the next heights of Xaniar and Abol
        next_h1 = (x1 * curr_h1 + y1) % m
        next_h2 = (x2 * curr_h2 + y2) % m
        # Increment the minimum time by 1
        min_time += 1
        # Update the current heights of Xaniar and Abol
        curr_h1, curr_h2 = next_h1, next_h2
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

