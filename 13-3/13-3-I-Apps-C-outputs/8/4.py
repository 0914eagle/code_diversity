
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0

    # Check if the rectangle can be placed on the initial field
    if a <= h and b <= w:
        return min_extensions

    # Sort the extensions in descending order
    extensions.sort(reverse=True)

    # Loop through the extensions and check if they can be used to enlarge the field
    for extension in extensions:
        # Check if the extension can be used to enlarge the width of the field
        if extension <= h:
            h *= extension
            min_extensions += 1

        # Check if the extension can be used to enlarge the length of the field
        if extension <= w:
            w *= extension
            min_extensions += 1

        # Check if the rectangle can be placed on the field after using the extension
        if a <= h and b <= w:
            return min_extensions

    # If the rectangle can't be placed on the field with all extensions, return -1
    return -1

