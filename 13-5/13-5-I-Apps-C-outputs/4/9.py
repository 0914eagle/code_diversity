
def get_min_extensions(a, b, h, w, n, extensions):
    # Sort the extensions in descending order
    extensions.sort(reverse=True)

    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0

    # Loop through the extensions and check if they can be used to enlarge the field
    for extension in extensions:
        # Check if the extension can be used to enlarge the width of the field
        if extension <= w:
            # Enlarge the width of the field by the extension
            w *= extension

            # Check if the rectangle can be placed on the field after enlarging the width
            if w >= a:
                # Break the loop and return the minimum number of extensions needed
                break

        # Check if the extension can be used to enlarge the length of the field
        if extension <= h:
            # Enlarge the length of the field by the extension
            h *= extension

            # Check if the rectangle can be placed on the field after enlarging the length
            if h >= b:
                # Break the loop and return the minimum number of extensions needed
                break

    # If the rectangle can be placed on the field, return the minimum number of extensions needed
    if w >= a and h >= b:
        return min_extensions

    # If the rectangle can't be placed on the field, return -1
    return -1

