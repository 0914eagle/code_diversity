
def solve(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0

    # If the rectangle can be placed on the initial field, return 0
    if a <= h and b <= w:
        return 0

    # Sort the extensions in descending order
    extensions.sort(reverse=True)

    # Iterate through the extensions
    for extension in extensions:
        # If the extension multiplies the width, multiply h by the extension
        if extension <= h:
            h *= extension
        # If the extension multiplies the length, multiply w by the extension
        elif extension <= w:
            w *= extension
        # If the extension is greater than both h and w, increase the minimum number of extensions needed
        else:
            min_extensions += 1

        # If the rectangle can be placed on the field, return the minimum number of extensions needed
        if a <= h and b <= w:
            return min_extensions

    # If the rectangle can't be placed on the field, return -1
    return -1

