
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    
    # Check if the rectangle can be placed on the initial field
    if a <= h and b <= w:
        return min_extensions
    
    # Sort the extensions in descending order
    extensions.sort(reverse=True)
    
    # Iterate through the extensions
    for extension in extensions:
        # Check if the extension can be used to enlarge the width or the length of the field
        if extension <= h or extension <= w:
            # Increase the minimum number of extensions needed
            min_extensions += 1
            # Decrease the size of the field by the extension
            h -= extension
            w -= extension
    
    # Check if the rectangle can be placed on the field after all the extensions are used
    if a <= h and b <= w:
        return min_extensions
    else:
        return -1

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

