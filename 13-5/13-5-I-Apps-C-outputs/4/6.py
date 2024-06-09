
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

            # Check if the rectangle can now be placed on the field
            if w >= a:
                # Return the minimum number of extensions needed
                return min_extensions

        # Check if the extension can be used to enlarge the length of the field
        if extension <= h:
            # Enlarge the length of the field by the extension
            h *= extension

            # Check if the rectangle can now be placed on the field
            if h >= b:
                # Return the minimum number of extensions needed
                return min_extensions

        # Increment the minimum number of extensions needed
        min_extensions += 1

    # If the rectangle cannot be placed on the field with all extensions, return -1
    return -1

