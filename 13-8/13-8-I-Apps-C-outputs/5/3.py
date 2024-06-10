
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0
    # Loop through each extension
    for extension in extensions:
        # Check if the extension can be used to enlarge the width or length of the field
        if extension <= w or extension <= h:
            # Increase the minimum number of extensions needed
            min_extensions += 1
            # Check if the rectangle can be placed on the field after enlarging it with the current extension
            if a * extension <= w and b * extension <= h:
                # If the rectangle can be placed on the field, return the minimum number of extensions needed
                return min_extensions
    # If the rectangle can't be placed on the field with all extensions, return -1
    return -1

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

