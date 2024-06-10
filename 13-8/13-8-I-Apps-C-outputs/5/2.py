
def get_extensions(a, b, h, w, n, extensions):
    # Initialize variables
    used_extensions = set()
    current_h = h
    current_w = w

    # Iterate through the extensions
    for i in range(n):
        # Check if the current extension is already used
        if i in used_extensions:
            continue

        # Check if the current extension can be used to enlarge the field
        if a * extensions[i] > current_h or b * extensions[i] > current_w:
            # Add the current extension to the used extensions set
            used_extensions.add(i)
            # Update the current field sizes
            current_h = max(current_h, a * extensions[i])
            current_w = max(current_w, b * extensions[i])

    # Check if the field is large enough to place the rectangle
    if current_h >= a and current_w >= b:
        return len(used_extensions)
    else:
        return -1

def main():
    a, b, h, w, n = map(int, input().split())
    extensions = list(map(int, input().split()))
    print(get_extensions(a, b, h, w, n, extensions))

if __name__ == '__main__':
    main()

