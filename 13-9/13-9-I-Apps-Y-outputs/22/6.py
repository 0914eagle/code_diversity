
def is_possible(height, width, bricks):
    # Initialize a list to store the number of bricks used in each layer
    layers = [0] * height
    # Iterate through the bricks and add them to the appropriate layer
    for brick in bricks:
        # Find the first layer that has enough space for the current brick
        for i in range(height):
            if layers[i] + brick <= width:
                layers[i] += brick
                break
        else:
            # If no layer has enough space, return False
            return False
    # If all bricks are used, return True
    return True

def main():
    height, width, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    print("YES") if is_possible(height, width, bricks) else print("NO")

if __name__ == '__main__':
    main()

