
def get_min_extensions(a, b, h, w, n, extensions):
    # Sort the extensions in descending order
    extensions.sort(reverse=True)

    # Initialize the minimum number of extensions needed to be 0
    min_extensions = 0

    # Loop through the extensions and check if they can be used to enlarge the field
    for extension in extensions:
        # Check if the extension can be used to enlarge the width of the field
        if extension <= w:
            # Increase the width of the field by the extension
            w *= extension

            # Check if the rectangle can be placed on the field after enlarging the width
            if w >= a:
                # Increase the minimum number of extensions needed
                min_extensions += 1

                # Break out of the loop since the rectangle can be placed on the field
                break

        # Check if the extension can be used to enlarge the length of the field
        if extension <= h:
            # Increase the length of the field by the extension
            h *= extension

            # Check if the rectangle can be placed on the field after enlarging the length
            if h >= b:
                # Increase the minimum number of extensions needed
                min_extensions += 1

                # Break out of the loop since the rectangle can be placed on the field
                break

    # Return the minimum number of extensions needed to reach Arkady's goal
    return min_extensions
