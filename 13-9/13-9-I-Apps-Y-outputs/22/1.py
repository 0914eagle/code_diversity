
def is_feasible(h, w, n, x):
    
    # Initialize the number of bricks used in each layer
    num_bricks_used = [0] * h
    # Initialize the number of bricks remaining
    num_bricks_remaining = n
    # Iterate through the layers
    for layer in range(h):
        # Iterate through the bricks in the current layer
        for i in range(num_bricks_remaining):
            # If the brick fits in the current layer
            if x[i] <= w - sum(num_bricks_used[layer:]):
                # Add the brick to the current layer
                num_bricks_used[layer] += 1
                # Subtract the brick from the number of bricks remaining
                num_bricks_remaining -= 1
                # Break out of the inner loop
                break
        # If all the bricks have been used and the layer is not complete
        if num_bricks_remaining == 0 and num_bricks_used[layer] != layer + 1:
            # The wall cannot be built
            return False
    # The wall can be built
    return True

def main():
    # Read the input
    h, w, n = map(int, input().split())
    x = list(map(int, input().split()))
    # Determine whether the wall can be built
    if is_feasible(h, w, n, x):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

