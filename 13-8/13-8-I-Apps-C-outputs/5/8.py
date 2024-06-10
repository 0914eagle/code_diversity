
def get_min_extensions(a, b, h, w, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    # If the rectangle can be placed on the initial field, return 0
    if a <= h and b <= w:
        return 0
    
    # Iterate through the available extensions
    for extension in extensions:
        # If the extension multiplies the width, multiply h by the extension
        if extension <= h:
            h *= extension
        # If the extension multiplies the length, multiply w by the extension
        elif extension <= w:
            w *= extension
        # If the extension multiplies both the width and the length, multiply both h and w by the extension
        else:
            h *= extension
            w *= extension
        
        # If the rectangle can be placed on the field after applying the extension, increment the minimum number of extensions needed
        if a <= h and b <= w:
            min_extensions += 1
    
    # Return the minimum number of extensions needed to reach Arkady's goal
    return min_extensions

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, extensions))

if __name__ == '__main__':
    main()

