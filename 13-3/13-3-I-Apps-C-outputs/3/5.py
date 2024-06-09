
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    # If the rectangle can be placed on the initial field, return 0
    if a <= h and b <= w:
        return 0
    
    # Iterate through the available extensions
    for i in range(n):
        # If the current extension multiplies the width, multiply h by a_i
        if extensions[i] == 1:
            h *= a[i]
        # If the current extension multiplies the length, multiply w by a_i
        else:
            w *= a[i]
        
        # If the rectangle can be placed on the field after applying the current extension, increment the minimum number of extensions needed
        if a <= h and b <= w:
            min_extensions += 1
    
    # Return the minimum number of extensions needed to reach Arkady's goal
    return min_extensions

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

