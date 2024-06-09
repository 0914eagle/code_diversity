
def find_min_moves(n_rows, n_cols, delete_icons, keep_icons, icons):
    
    # Initialize a set to store the icons that are in the delete rectangle
    delete_rectangle = set()

    # Loop through each icon in the delete_icons list
    for icon in delete_icons:
        # Check if the icon is in the delete rectangle
        if icon in delete_rectangle:
            # If the icon is already in the delete rectangle, continue to the next icon
            continue
        # Add the icon to the delete rectangle
        delete_rectangle.add(icon)
        # Check if the icon overlaps with any of the keep icons
        for keep_icon in keep_icons:
            # If the icon overlaps with a keep icon, remove it from the delete rectangle
            if icon.overlaps(keep_icon):
                delete_rectangle.remove(icon)
                break

    # Initialize a set to store the icons that are not in the delete rectangle
    not_delete_rectangle = set(icons) - delete_rectangle

    # Initialize a variable to store the minimum number of moves
    min_moves = 0

    # Loop through each icon in the not_delete_rectangle set
    for icon in not_delete_rectangle:
        # Check if the icon is in the delete rectangle
        if icon in delete_rectangle:
            # If the icon is in the delete rectangle, continue to the next icon
            continue
        # Add the icon to the delete rectangle
        delete_rectangle.add(icon)
        # Increment the minimum number of moves
        min_moves += 1

    return min_moves

def main():
    # Read the input from stdin
    n_rows, n_cols, n_delete, n_keep = map(int, input().split())
    delete_icons = [int(x) for x in input().split()]
    keep_icons = [int(x) for x in input().split()]
    icons = [int(x) for x in input().split()]

    # Call the find_min_moves function and print the result
    print(find_min_moves(n_rows, n_cols, delete_icons, keep_icons, icons))

if __name__ == '__main__':
    main()

