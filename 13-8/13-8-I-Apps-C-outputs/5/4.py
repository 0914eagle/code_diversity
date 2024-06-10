
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    
    # Check if the rectangle can be placed on the initial field
    if a <= h and b <= w:
        return min_extensions
    
    # Iterate through the available extensions
    for i in range(n):
        # Check if the extension can be applied
        if extensions[i] <= h or extensions[i] <= w:
            # Apply the extension
            h *= extensions[i]
            w *= extensions[i]
            # Increment the minimum number of extensions needed
            min_extensions += 1
            # Check if the rectangle can be placed on the field after applying the extension
            if a <= h and b <= w:
                return min_extensions
    
    # If the rectangle can't be placed on the field with all extensions, return -1
    return -1

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

