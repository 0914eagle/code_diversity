
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    # Loop through each extension
    for extension in extensions:
        # Check if the extension multiplies the width
        if extension > w:
            # Multiply the width by the extension
            w *= extension
            # Increment the minimum number of extensions needed
            min_extensions += 1
        # Check if the extension multiplies the length
        elif extension > h:
            # Multiply the length by the extension
            h *= extension
            # Increment the minimum number of extensions needed
            min_extensions += 1
    # Check if the rectangle can be placed on the field
    if a <= w and b <= h:
        # Return the minimum number of extensions needed
        return min_extensions
    else:
        # Return -1 if the rectangle can't be placed on the field
        return -1

def main():
    # Read the input
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    # Call the get_min_extensions function and print the result
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

