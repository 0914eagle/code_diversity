
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    # If the rectangle can be placed on the initial field, return 0
    if a <= h and b <= w:
        return 0
    # Otherwise, iterate through the available extensions
    for i in range(n):
        # If the i-th extension multiplies the width of the field by a_{i}
        if extensions[i] <= h:
            # Multiply the width of the field by a_{i}
            h *= extensions[i]
            # If the rectangle can now be placed on the field, return the current minimum number of extensions
            if a <= h and b <= w:
                return min_extensions
        # If the i-th extension multiplies the length of the field by a_{i}
        if extensions[i] <= w:
            # Multiply the length of the field by a_{i}
            w *= extensions[i]
            # If the rectangle can now be placed on the field, return the current minimum number of extensions
            if a <= h and b <= w:
                return min_extensions
        # Otherwise, increment the minimum number of extensions needed
        min_extensions += 1
    # If the rectangle can't be placed on the field with all extensions, return -1
    return -1

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

