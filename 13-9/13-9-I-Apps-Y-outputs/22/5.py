
def is_possible(h, w, n, x):
    # Initialize variables
    layers = [0] * h
    layer_width = 0
    brick_idx = 0
    brick_width = x[brick_idx]

    # Loop through each layer
    for layer in range(h):
        # Loop through each brick in the layer
        while brick_idx < n and layer_width + brick_width <= w:
            # Add the brick to the layer
            layers[layer] += brick_width
            layer_width += brick_width
            brick_idx += 1
            if brick_idx < n:
                brick_width = x[brick_idx]

        # If the layer is not complete, return False
        if layer_width < w:
            return False

        # Reset the layer width and brick index for the next layer
        layer_width = 0
        brick_idx = 0
        brick_width = x[brick_idx]

    # If all layers are complete, return True
    return True

def main():
    h, w, n = map(int, input().split())
    x = list(map(int, input().split()))
    print("YES") if is_possible(h, w, n, x) else print("NO")

if __name__ == '__main__':
    main()

