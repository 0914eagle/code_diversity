
def get_min_extensions(a, b, h, w, n, extensions):
    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0

    # Check if the rectangle can be placed on the initial field
    if a <= h and b <= w:
        return 0

    # Sort the extensions in descending order
    extensions.sort(reverse=True)

    # Loop through the extensions
    for extension in extensions:
        # Check if the extension multiplies the width or the length by a factor that is greater than or equal to the ratio of the rectangle's width or length to the field's width or length
        if extension >= max(a / h, b / w):
            # Increment the minimum number of extensions needed
            min_extensions += 1
            # Update the field sizes
            h *= extension
            w *= extension

    # Check if the rectangle can be placed on the field after using all the extensions
    if a <= h and b <= w:
        return min_extensions
    else:
        return -1

